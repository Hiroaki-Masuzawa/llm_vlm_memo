import base64

import requests
from openai import OpenAI


# def encode_base64_content_from_url(content_url: str) -> str:
#     """Encode a content retrieved from a remote url to base64 format."""

#     with requests.get(content_url) as response:
#         response.raise_for_status()
#         result = base64.b64encode(response.content).decode('utf-8')

#     return result


# # Text-only inference
# def run_text_only(client, model, text, max_completion_tokens=128) -> None:
#     chat_completion = client.chat.completions.create(
#         messages=[{
#             "role": "user",
#             "content": text
#         }],
#         model=model,
#         max_completion_tokens=max_completion_tokens,
#     )

#     result = chat_completion.choices[0].message.content
#     print("Chat completion output:", result)


# # https://qiita.com/ydclab_0031/items/7d3b0a7928d3805d0647
# def encode_image(image_path):
#   with open(image_path, "rb") as image_file:
#     return base64.b64encode(image_file.read()).decode('utf-8')

# opencv ver
import cv2
def np_to_base64(image):
    # 画像をPNG形式にエンコード
    _, buffer = cv2.imencode('.png', image)
    
    # バッファをBase64文字列に変換
    base64_bytes = base64.b64encode(buffer)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string

def image_to_base64(image_path):
    # 画像を読み込む
    img = cv2.imread(image_path)
    # Base64変換
    return np_to_base64(img)

# # Single-image input inference
# def run_single_image(client, model, text, image_path, max_completion_tokens=128) -> None:
#     ## Use base64 encoded image in the payload

#     # image_base64 = encode_base64_content_from_url(image_url)
#     # image_base64 = encode_image("image_path")
#     image_base64 = image_to_base64(image_path)
#     chat_completion_from_base64 = client.chat.completions.create(
#         messages=[
#             # {"role": "system", "content": "Please answer using Japanese."},
#             {
#             "role":
#                 "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": text,
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/png;base64,{image_base64}"
#                     },
#                 },
#             ],
#         }],
#         model=model,
#         max_completion_tokens=max_completion_tokens,
#     )

#     result = chat_completion_from_base64.choices[0].message.content
#     print("Chat completion output from base64 encoded image:", result)


import argparse


if __name__ == "__main__" and False:
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, default="") 
    parser.add_argument('--image_path', type=str, default="") 
    parser.add_argument('--server', type=str, default="localhost") 
    parser.add_argument('--port', type=int, default=8000) 
    args = parser.parse_args() 
    # print(args) 

    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "sk-dummy"
    openai_api_base = "http://{}:{}/v1".format(args.server, args.port)

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    models = client.models.list()
    model = models.data[0].id

    # print(model)

    # if args.image_path == "":
    #     run_text_only(client, model, args.text)
    # else :
    #     run_single_image(client, model, args.text, args.image_path)


if __name__=='__main__':
    import base64
    from openai import OpenAI
    import cv2



    openai_api_key = "sk-dummy"
    openai_api_base = "http://{}:{}/v1".format("localhost", 8000)

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    models = client.models.list()
    model = models.data[0].id
    print(model)
    image_base64_1 = image_to_base64("sample2.png")

    chat_completion_from_base64 = client.chat.completions.create(model=model, 
                                                                max_completion_tokens=256, 
                                                                messages=[
                                                                    {"role":"user", 
                                                                    "content": [
                                                                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64_1}"} },
                                                                        {"type":"text", "text": "There are seven blocks."}
                                                                        ]
                                                                        }
                                                                        ]
                                                                        )
    responce  = chat_completion_from_base64.choices[0].message.content
    finish_reason = chat_completion_from_base64.choices[0].finish_reason
    print(responce, finish_reason)
    # if finish_reason=="length" :
    #     chat_completion_from_base64_2 = client.chat.completions.create(model=model, 
    #                                     max_completion_tokens=256, 
    #                                     messages=[
    #                                         {   "role":"user", 
    #                                             "content": [
    #                                             {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64_1}"} },
    #                                             {"type":"text", "text": "What are there in the image?"}
    #                                             ]
    #                                         },
    #                                         {
    #                                             "role": "assistant", "content": responce
    #                                         }
    #                                         ]
    #                                     )


    image_base64_2 = image_to_base64("image_000251.png")


    chat_completion_from_base64_2 = client.chat.completions.create(model=model, 
                                    max_completion_tokens=256, 
                                    messages=[
                                        {   "role":"user", 
                                            "content": [
                                            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64_1}"} },
                                            {"type":"text", "text": "What are there in the image?"}
                                            ]
                                        },
                                        {
                                            "role": "assistant", "content": responce
                                        },
                                        {
                                            "role":"user", 
                                            "content": [
                                                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64_2}"} },
                                                {"type":"text", "text": "What number block in the first image does this block appear to match?  Please answer with the number only."}
                                            ]
                                        }
                                        ]
                                    )

    finish_reason_2 = chat_completion_from_base64_2.choices[0].finish_reason
    print(finish_reason_2)


    responce_2  = chat_completion_from_base64_2.choices[0].message.content
    print(responce_2)