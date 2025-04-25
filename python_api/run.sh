SCRIPT_DIR=$(cd $(dirname $0); pwd)
docker run -it --rm \
    --net=host \
    -u `id -u`:`id -g` \
    -v /etc/passwd:/etc/passwd:ro \
    -v /etc/group:/etc/group:ro \
    -v ${SCRIPT_DIR}:/userdir -w /userdir \
    --name python_openai \
    python_openai bash