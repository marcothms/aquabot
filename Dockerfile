FROM python:3.8-alpine

WORKDIR /data
COPY . /data

RUN apk add .build-deps gcc libc-dev \
    apk add ffmpeg \
    && python3 -m pip install -r requirements.txt

ENV PREFIX /data
ENV TOKEN /data
ENV REDDIT_CLIENT_ID /data
ENV REDDIT_CLIENT_SECRET /data
ENV REDDIT_CLIENT_USERAGENT /data

CMD [ "python3", "./aquabot.py" ]