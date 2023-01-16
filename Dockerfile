FROM ubuntu:22.04

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    requests 

COPY . src

CMD [ "/bin/bash", "-c", "python3 src/smhi_obs/examples/get_yesterdays_temperature.py"]
