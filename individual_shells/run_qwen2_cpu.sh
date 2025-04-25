SCRIPT_DIR=$(cd $(dirname $0); pwd)
CACHEDIR=${SCRIPT_DIR}/../vllm_root_cache
docker run --rm \
  --ipc=host --network=host \
  --rm --name qwen2.5 -it \
  -v ${CACHEDIR}:/root/.cache \
  vllm-cpu-env \
  --model Qwen/Qwen2-VL-2B-Instruct --served-model-name Qwen2-VL-2B-Instruct