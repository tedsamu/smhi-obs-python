# Containerized Development Environment
These are instructions for creation and usage of a simple docker container to enable you to easy test and develop the smhi-obs package.

To build the development docker image:
```
docker build -t smhi_obs_python .
```

To run the development container:
```
xhost +
docker run -it --rm --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --volume="$PWD/../:/usr/src/app/src" smhi_obs_python /bin/bash
```

To start pycharm (inside container):
```
./pycharm src
```

To run all tests including coverage report (inside container):
```
cd /usr/src/app/src
pytest --cov
```

To run type checker (inside container):
```
cd /usr/src/app/src
mypy --disallow-untyped-defs .
```
