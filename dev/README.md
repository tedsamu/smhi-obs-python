# Containerized Development Environment
These are instructions for creation and usage of a simple docker container to enable you to easy test and develop the smhi-obs package.

To build the runtime docker image:
```
docker build -t smhi_obs_python --target smhi_obs .
```

To run the `get_yesterdays_temperature.py` example:
```
docker run --rm --volume="$PWD/../:/usr/src/app/src" smhi_obs_python 
```

To enter the container to test out other things, run:
```
docker run --rm -it --volume="$PWD/../:/usr/src/app/src" smhi_obs_python /bin/bash
```

## Development container
The development version of the container includes all dependencies for testing as well as Pycharm CE.

To build the development docker image:
```
docker build -t smhi_obs_python_dev .
```

To run the development container:
```
xhost +            # Allow access to X
docker run -it --rm --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --volume="$PWD/../:/usr/src/app/src" smhi_obs_python_dev /bin/bash
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

To run flake8 linter (inside container):
```
cd /usr/src/app/src
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

