FROM ubuntu:22.04 AS smhi_obs

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    requests 

CMD [ "/bin/bash", "-c", "python3 src/smhi_obs/examples/get_yesterdays_temperature.py"]

FROM SMHI_OBS AS smhi_obs_dev

RUN apt-get update && apt-get install -y \
    curl \
    libxrender1 \
    libxtst6 \
    libxi6 \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    types-requests \
    pytest \
    pytest-mock \
    pytest-cov \
    mypy \
    flake8

RUN ["/bin/bash", "-c", "set -o pipefail && curl -L https://download.jetbrains.com/python/pycharm-community-2022.1.1.tar.gz  | tar -xvz && ln -s pycharm-community-2022.1.1/bin/pycharm.sh pycharm"]
