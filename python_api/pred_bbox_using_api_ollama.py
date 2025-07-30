import base64
from openai import OpenAI
import cv2


def np_to_base64(image):
    # 画像をPNG形式にエンコード
    _, buffer = cv2.imencode(".png", image)

    # バッファをBase64文字列に変換
    base64_bytes = base64.b64encode(buffer)
    base64_string = base64_bytes.decode("utf-8")
    return base64_string


def image_to_base64(image_path):
    # 画像を読み込む
    img = cv2.imread(image_path)
    # Base64変換
    return np_to_base64(img)


if __name__ == "__main__":
    hostname="localhost"
    portnumber=8000 #11434
    openai_api_key = "sk-dummy"
    openai_api_base = "http://{}:{}/v1".format(hostname, portnumber)

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=openai_api_key,
        base_url=openai_api_base,
    )

    models = client.models.list()
    # model = "qwen2.5vl:7b-fp16"
    # model = "qwen2.5vl:7b-q8_0"
    model = models.data[0].id
    print(model)


    system_prompt = """
    You are a helpful assistant. When detecting objects in an image, output the result in valid JSON format.

    The output must be a JSON array (list). Each item in the array must be a JSON object containing:
    - a "label" field: a string that describes the name of the detected object (e.g., "door", "window").
    - a "bbox_2d" field: an array of four integers [x1, y1, x2, y2] representing the bounding box in pixels.

    If multiple objects are found, include one object per item in the JSON array.

    The response must be only the JSON — do not include any explanation, markdown formatting, or additional text outside the JSON block.
    """.strip()


    image_file = "cans.jpg"
    image_base64_1 = image_to_base64(image_file)

    chat_completion_from_base64 = client.chat.completions.create(
        model=model,
        max_completion_tokens=256,
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": system_prompt #"You are a helpful assistant." #" When output a bounding box of the object in the image, the bounding box should start with <|box_start|> and end with <|box_end|>.",
                    },
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{image_base64_1}"},
                    },
                    {"type": "text", "text": "Detect the bounding box of red can."},
                ],
            },
        ],
        extra_body={"skip_special_tokens": False},
    )
    responce = chat_completion_from_base64.choices[0].message.content
    finish_reason = chat_completion_from_base64.choices[0].finish_reason
    print(responce, finish_reason)


    img = cv2.imread(image_file)
    cv2.rectangle(img, [437, 198], [516, 387], (255,0,0))
    cv2.imwrite("output.png", img)