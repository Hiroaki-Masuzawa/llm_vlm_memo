import base64
from openai import OpenAI
import cv2


# opencv ver
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


if __name__=='__main__':
    
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

    max_completion_tokens=1024
    messages = list()
    chats = []


    image_base64_1 = image_to_base64("sample2.png")
    messages.append({"role":"user", 
                    "content": [
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64_1}"} },
                        {"type":"text", "text": "There are seven blocks. Number them from top left to bottom right."}
                        ]
                        }
                        )
    chats.append( client.chat.completions.create(model=model, 
                                            max_completion_tokens=max_completion_tokens,
                                            messages = messages)
    )
    responce  = chats[-1].choices[0].message.content
    finish_reason = chats[-1].choices[0].finish_reason
    print(responce)
    print(finish_reason)

    messages.append(
                    {
                        "role": "assistant",
                        "content": responce
                    }
                    )
    image_base64_2 = image_to_base64("image_001251.png")
    messages.append(
                    {
                        "role":"user", 
                        "content": [
                            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64_2}"} },
                            {"type":"text", "text": "Which block in the first image does this block appear to be colour-matched to?"}
                            ]
                    }
                    )
    # Please answer with the number only.
    chat2 = client.chat.completions.create(model=model, 
                                            max_completion_tokens=max_completion_tokens,
                                            messages = messages)
    finish_reason_2 = chat2.choices[0].finish_reason
    print(finish_reason_2)


    responce_2  = chat2.choices[0].message.content
    print(responce_2)