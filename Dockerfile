FROM python:3.8

RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /data

COPY . /data

ENV PREFIX /data
ENV TOKEN /data
ENV REDDIT_CLIENT_ID /data
ENV REDDIT_CLIENT_SECRET /data
ENV REDDIT_CLIENT_USERAGENT /data

RUN python3 -m pip install -r requirements.txt

CMD python3 aquabot.py
