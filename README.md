# 準備
## ollama
```
docker pull ollama/ollama
```
## vllm
```
ghcr.io/open-webui/open-webui:main
```
### GPU
```
docker pull vllm/vllm-openai:latest
```
### CPU
```
cd vllm
docker build -f docker/Dockerfile.cpu --tag vllm-cpu-env --target vllm-openai .
cd ..
```

# 実行
## サーバ側
### ollama
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
### vllm
以下適切なものを選ぶ
- Qwen2-VL-2B (GPU)
    ```
    ./run_qwen2.sh
    ```
- Qwen2-VL-7B (CPU)
    ```
    ./run_qwen2-7b_cpu.sh
    ```
- llava-1.5-7b (GPU)
    ```
    ./run_llava-1.5-7b-hf.sh
    ```
- 

## クライアント側
### CUI (ollama - llama3)
1. 端末で実行
```
exec_llama3.sh
```
### webUI (ollama, vllm)
1. 端末で実行
    ```
    docker run -d -p 5955:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
    ```
2. http://localhost:5955 にアクセスする．

### python
- ollama
以下を参考にする．
https://www.ollama.com/blog/openai-compatibility
- vllm
以下が参考になる．
https://qiita.com/engchina/items/f7cc32f3f34011b69a18#api%E3%83%AA%E3%82%AF%E3%82%A8%E3%82%B9%E3%83%88%E3%81%AE%E9%80%81%E4%BF%A1