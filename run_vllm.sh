SCRIPT_DIR=$(cd $(dirname $0); pwd)
CACHEDIR=${SCRIPT_DIR}/vllm_root_cache
MODEL=Qwen/Qwen2-VL-2B-Instruct
SERVEDMODEL=Qwen2-VL-2B-Instruct
GPUOPTION="--gpus all"
IMAGE_NAME=vllm/vllm-openai:latest
OPTIONS=""

while [[ $# -gt 0 ]]; do
    case $1 in
        # -D|--devel)
        #     USE_DEVEL="yes"
        #     shift
        #     ;;
        -m|--model)
            case $2 in
                qwen2)
                    MODEL=Qwen/Qwen2-VL-2B-Instruct
                    SERVEDMODEL=Qwen2-VL-2B-Instruct
                    ;;
                qwen2-7b)
                    MODEL=Qwen/Qwen2-VL-7B-Instruct
                    SERVEDMODEL=Qwen2-VL-7B-Instruct
                    ;;
                qwen2.5)
                    MODEL=Qwen/Qwen2.5-VL-3B-Instruct
                    SERVEDMODEL=Qwen2.5-VL-3B-Instruct
                    OPTIONS+=" --max_model_len 87360"   ## VLAM 16GB設定
                    ;;
                llava-1.5)
                    MODEL=llava-hf/llava-1.5-7b-hf
                    SERVEDMODEL=llava-1.5-7b-hf
                    OPTIONS+=" --chat-template /vllm/examples/template_llava.jinja --gpu_memory_utilization 0.95 --max_model_len 1024"   ## VLAM 16GB設定
                    ;;
                blip2)
                    MODEL=Salesforce/blip2-opt-2.7b
                    SERVEDMODEL=blip2-opt-2.7b
                    OPTIONS+=" --chat-template /vllm/examples/template_blip2.jinja"
                    ;;
                blip2-6.7b)
                    MODEL=Salesforce/blip2-opt-6.7b
                    SERVEDMODEL=blip2-opt-6.7b
                    OPTIONS+=" --chat-template /vllm/examples/template_blip2.jinja"
                    ;;
                *)
                    echo "Unknown model $2"
                    exit 1
                    ;;
            esac
            shift
            shift
            ;;
        -G|--no-gpu)
            IMAGE_NAME="vllm-cpu-env"
            GPUOPTION=" "
            shift
            ;;
        --)
            shift
            break
            ;;
        -*|--*)
            echo "Unknown option $1"
            exit 1
            ;;
        # *)
        #     POSITIONAL_ARGS+=("$1") # save positional arg
        #     shift # past argument
        #     ;;
    esac
done

set -x
docker run -it --rm \
  ${GPUOPTION}\
  --ipc=host --network=host \
  --name vllm_api_server \
  -v ${CACHEDIR}:/root/.cache \
  -v ${SCRIPT_DIR}/vllm:/vllm \
  ${IMAGE_NAME} \
  --model ${MODEL} --served-model-name ${SERVEDMODEL} ${OPTIONS}