FROM python:3.6

MAINTAINER Marco Thomas

RUN mkdir /aquabot-docker
WORKDIR /aquabot-docker
COPY . /aquabot-docker

RUN pip install --user -r requirements.txt

CMD ["python", "aquabot.py"]
