To build the development docker image:
```
docker build -t easy_smhi_python .
```

To run the development container:
```
xhost +
docker run -it --rm --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --volume="$PWD/../:/usr/src/app/src" easy_smhi_python /bin/bash
```

To start pycharm:
```
./pycharm src
```

To run all tests including coverage report:
```
cd /usr/src/app/src
pytest --cov
```

To run type checker:
```
cd /usr/src/app/src
mypy --disallow-untyped-defs .
```
