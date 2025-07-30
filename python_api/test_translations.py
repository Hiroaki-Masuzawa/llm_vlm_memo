from openai import OpenAI
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio_path", type=str, default="")
    parser.add_argument("--server", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--model", type=str, default="whisper-small")

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

    # 音声ファイルの準備
    audio_file = open(args.audio_path, "rb")

    # 推論の実行
    transcription = client.audio.translations.create(
        model=args.model, file=audio_file
    )
    print(transcription.text)
