SCRIPT_DIR=$(cd $(dirname $0); pwd)
CACHEDIR=${SCRIPT_DIR}/../vllm_root_cache
MODEL=Qwen/Qwen2.5-VL-3B-Instruct

docker run --rm --network=host \
    -v ${CACHEDIR}:/root/.cache \
    --ipc=host \
    -v ${SCRIPT_DIR}/../vllm:/vllm \
    vllm-cpu-env \
    --model ${MODEL} --served-model-name Qwen2.5-VL-3B-Instruct --max_model_len 116480

