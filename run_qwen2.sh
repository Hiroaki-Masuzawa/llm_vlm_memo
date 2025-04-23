CACHEDIR=${PWD}/vlm_root_cache
docker run --gpus all \
  --ipc=host --network=host \
  --rm --name qwen2.5 -it \
  -v ${CACHEDIR}:/root/.cache \
  vllm/vllm-openai:latest \
  --model Qwen/Qwen2-VL-2B-Instruct --served-model-name Qwen2-VL-2B-Instruct --max_model_len 6752