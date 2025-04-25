CACHEDIR=${PWD}/vllm_root_cache
docker run \
  --ipc=host --network=host \
  --rm --name qwen2.5 -it \
  -v ${CACHEDIR}:/root/.cache \
  vllm-cpu-env \
  --model Qwen/Qwen2-VL-2B-Instruct --served-model-name Qwen2-VL-2B-Instruct