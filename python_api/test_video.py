from openai import OpenAI

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
models = client.models.list()
model = models.data[0].id
print(model)

video_url = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"

## Use video url in the payload
chat_completion_from_url = client.chat.completions.create(
    messages=[{
        "role":
        "user",
        "content": [
            {
                "type": "text",
                "text": "What's in this video?"
            },
            {
                "type": "video_url",
                "video_url": {
                    "url": video_url
                },
            },
        ],
    }],
    model=model,
    max_completion_tokens=256,
)

result = chat_completion_from_url.choices[0].message.content
print("Chat completion output from video url:", result)