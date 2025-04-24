CACHEDIR=${PWD}/vllm_root_cache
MODEL=Qwen/Qwen2-VL-7B-Instruct

docker run --network=host \
    -v ${CACHEDIR}:/root/.cache \
    --ipc=host \
    -v ${PWD}/vllm:/vllm \
    vllm-cpu-env \
    --model ${MODEL}

