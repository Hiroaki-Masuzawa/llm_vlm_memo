SCRIPT_DIR=$(cd $(dirname $0); pwd)
CACHEDIR=${SCRIPT_DIR}/../vllm_root_cache
docker run --rm --gpus all \
  --ipc=host --network=host \
  --rm --name whisper-small -it \
  -v ${CACHEDIR}:/root/.cache \
  --entrypoint="" \
  vllm/vllm-openai:latest bash -c "pip install vllm[audio] && vllm serve openai/whisper-small --served-model-name whisper-small" 