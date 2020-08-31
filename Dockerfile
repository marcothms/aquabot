FROM python:3.8

WORKDIR /data

COPY . /data

ENV PREFIX
ENV TOKEN
ENV REDDIT_CLIENT_ID
ENV REDDIT_CLIENT_SECRET
ENV REDDIT_CLIENT_USERAGENT

RUN python3 -m pip install -r requirements.txt

CMD python3 aquabot.py --prefix=$PREFIX --token=$TOKEN --reddit_client_id=$REDDIT_CLIENT_ID --reddit_client_secret=$REDDIT_CLIENT_SECRET --reddit_client_useragent=$REDDIT_CLIENT_USERAGENT
