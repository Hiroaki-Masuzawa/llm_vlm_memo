
import argparse
import cv2
import re

from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
try:
    from qwen_vl_utils import process_vision_info
except:
    import pip, site, importlib
    pip.main(['install', 'qwen_vl_utils'])
    importlib.reload(site) 
    from qwen_vl_utils import process_vision_info


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--object', type=str, default="red can") 
    parser.add_argument('--image_path', type=str, default="cans.jpg") 
    parser.add_argument('--model_path', type=str, default="/userdir/vllm_root_cache/huggingface/hub/models--Qwen--Qwen2-VL-7B-Instruct/snapshots/eed13092ef92e448dd6875b2a00151bd3f7db0ac/") 
    parser.add_argument('--output', type=str, default="") 
    args = parser.parse_args() 

    # model_pathについて
    # 別途vllm等でファイルをダウンロードしている場合はここにweightがある
    # ない場合は以下手順でダウンロードし，--model_path Qwen2-VL-2B-Instruct とオプションを入れる
    # $ git lfs install
    # $ git clone https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct

    data_path = args.model_path

    # default: Load the model on the available device(s)
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        data_path, torch_dtype="auto", device_map="auto"
    )

    # default processer
    processor = AutoProcessor.from_pretrained(data_path)

    image_file = args.image_path # 対象画像
    OBJECT = args.object # 対象物体
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": image_file,
                },
                {
                    "type": "text",
                    "text": f"Detect the bounding box of '{OBJECT}'."
                },
            ],
        }
    ]



    # Preparation for inference
    text = processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    # LLMが半分回答した状態にして続きを生成するようにする．
    text += f"<|object_ref_start|>{OBJECT}<|object_ref_end|><|box_start|>"


    image_inputs, video_inputs = process_vision_info(messages)

    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )
    inputs = inputs.to("cuda")

    # Inference: Generation of the output
    generated_ids = model.generate(**inputs, max_new_tokens=1024)
    generated_ids_trimmed = [
        out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    print(output_text[0])

    poses = output_text[0].replace("(","").replace(")","").split(',')
    if args.output != "" and len(poses)>=4:
        img = cv2.imread(args.image_path)
        h, w = img.shape[0:2]
        x_s = int(int(poses[0])/1000*w)
        y_s = int(int(poses[1])/1000*h)
        x_e = int(int(poses[2])/1000*w)
        y_e = int(int(poses[3])/1000*h)
        img2 = cv2.rectangle(img, (x_s,y_s), (x_e,y_e), (0,0,255), 3)
        cv2.imwrite(args.output, img2)
