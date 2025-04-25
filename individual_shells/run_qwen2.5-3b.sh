SCRIPT_DIR=$(cd $(dirname $0); pwd)
CACHEDIR=${SCRIPT_DIR}/../vllm_root_cache
MODEL=Qwen/Qwen2.5-VL-3B-Instruct

docker run --rm --gpus all \
    --network=host \
    -v ${CACHEDIR}:/root/.cache \
    --ipc=host \
    -v ${SCRIPT_DIR}/../vllm:/vllm \
    vllm/vllm-openai:latest \
    --model ${MODEL} --served-model-name Qwen2.5-VL-3B-Instruct --max_model_len 87360

