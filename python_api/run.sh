docker run -it --rm \
    --net=host \
    -u `id -u`:`id -g` \
    -v /etc/passwd:/etc/passwd:ro \
    -v /etc/group:/etc/group:ro \
    -v ${PWD}:/userdir -w /userdir \
    python_openai bash