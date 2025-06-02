import base64
import requests
from openai import OpenAI
# try:
#     from vllm.assets.audio import AudioAsset
# except:
#     import pip, site, importlib
#     pip.main(['install', 'vllm'])
#     importlib.reload(site) 
#     from vllm.assets.audio import AudioAsset

def encode_base64_content_from_url(content_url: str) -> str:
    """Encode a content retrieved from a remote url to base64 format."""

    with requests.get(content_url) as response:
        response.raise_for_status()
        result = base64.b64encode(response.content).decode('utf-8')

    return result

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id
print(model)


# Any format supported by librosa is supported
audio_url = AudioAsset("winning_call").url
audio_base64 = encode_base64_content_from_url(audio_url)

chat_completion_from_base64 = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "What's in this audio?"
            },
            {
                "type": "input_audio",
                "input_audio": {
                    "data": audio_base64,
                    "format": "wav"
                },
            },
        ],
    }],
    model=model,
    max_completion_tokens=64,
)

result = chat_completion_from_base64.choices[0].message.content
print("Chat completion output from input audio:", result)