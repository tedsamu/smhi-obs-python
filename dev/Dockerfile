FROM ubuntu:22.04

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    python3-pip \
    curl \
    libxrender1 \
    libxtst6 \
    libxi6 \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir \
    requests \
    types-requests \
    pytest \
    pytest-mock \
    pytest-cov \
    mypy
RUN ["/bin/bash", "-c", "set -o pipefail && curl -L https://download.jetbrains.com/python/pycharm-community-2022.1.1.tar.gz  | tar -xvz && ln -s pycharm-community-2022.1.1/bin/pycharm.sh pycharm"]


CMD [ "ls" ]
