FROM python:3.8-alpine

RUN apk add ffmpeg \
    && python3 -m pip install -r requirements.txt

WORKDIR /data
COPY . /data

ENV PREFIX /data
ENV TOKEN /data
ENV REDDIT_CLIENT_ID /data
ENV REDDIT_CLIENT_SECRET /data
ENV REDDIT_CLIENT_USERAGENT /data

CMD [ "python3", "./aquabot.py" ]