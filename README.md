![Avatar](https://i.imgur.com/pZDyR3h.jpg)

AquaBot
=======

[![discordpy](https://img.shields.io/badge/discordpy-Core-blue)](https://github.com/Rapptz/discord.py)

This Bot was created with the intention to be used on my own server.

## docker

+ Create a docker image with tag 'latest': `docker build . -t aquabot`
+ Copy `docker-compose.yml.example` to `docker-compose.yml`
+ Edit the required environment variables (Found in `aquabot.py`)
+ Start the bot: `docker-compose up -d`

## Requirements
+ python>=3.6.0
