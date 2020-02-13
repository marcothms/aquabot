FROM python:3.6

RUN mkdir /aquabot-docker
WORKDIR /aquabot-docker
COPY . /aquabot-docker

RUN pip install --user -r requirements.txt

CMD ["python3", "aquabot.py"]
