SCRIPT_DIR=$(cd $(dirname $0); pwd)
docker run -d --gpus=all -v ${SCRIPT_DIR}/../ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama