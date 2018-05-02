FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    python \
    python-setuptools \
    python-pip \
    graphicsmagick

ADD . /image-compare-output
WORKDIR /image-compare-output

COPY . .

CMD [ "python", "-u", ./imageCompare.py" ]
