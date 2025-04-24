CACHEDIR=${PWD}/vllm_root_cache

docker run --gpus all --network=host \
    -v ${CACHEDIR}:/root/.cache \
    --ipc=host \
    -v ${PWD}/vllm:/vllm \
    vllm/vllm-openai:latest \
    --model llava-hf/llava-1.5-7b-hf --chat-template /vllm/examples/template_llava.jinja --gpu_memory_utilization 0.95 --max_model_len 1024

