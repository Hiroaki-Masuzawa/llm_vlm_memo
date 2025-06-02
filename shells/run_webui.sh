SCRIPT_DIR=$(cd $(dirname $0); pwd)
WEBUI_DIR=${SCRIPT_DIR}/../open-webui
docker run -d -p 5955:8080 --add-host=host.docker.internal:host-gateway -v ${WEBUI_DIR}:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main