docker run -it -u `id -u`:`id -g` --net=host -v ${PWD}:/userdir -w /userdir node:24.2.0 bash
