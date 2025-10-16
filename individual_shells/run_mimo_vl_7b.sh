SCRIPT_DIR=$(cd $(dirname $0); pwd)
CACHEDIR=${SCRIPT_DIR}/../vllm_root_cache

docker run --rm --network=host \
    -v ${CACHEDIR}:/root/.cache \
    --ipc=host \
    -v ${SCRIPT_DIR}/../vllm:/vllm \
    vllm-cpu-env \
    --model 'XiaomiMiMo/MiMo-VL-7B-RL-2508' --max-model-len 22k
