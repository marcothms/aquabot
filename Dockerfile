FROM python:3.9

WORKDIR /data
COPY . /data

RUN apt update && apt install -y ffmpeg libopus0 opus-tools \
    && python3 -m pip install -r requirements.txt

ENV PREFIX /data
ENV TOKEN /data
ENV REDDIT_CLIENT_ID /data
ENV REDDIT_CLIENT_SECRET /data
ENV REDDIT_CLIENT_USERAGENT /data

CMD [ "python3", "./aquabot.py" ]
