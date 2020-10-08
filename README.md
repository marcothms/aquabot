![Avatar](https://i.imgur.com/pZDyR3h.jpg)

AquaBot
=======

[![discordpy](https://img.shields.io/badge/discordpy-Core-blue)](https://github.com/Rapptz/discord.py)

This Bot was created with the intention to be used on my own server.

## docker

Create a docker image with tag 'latest'
`docker build . -t aquabot`

In the correct path, create a docker-compose.yml and start the bot
The required env vars are found in 'aquabot.py'
`docker-compose up -d`

## Commands

The following commands assume that `.` is your prefix.

There are currently two command, which help the user to naviagte the bot's
commands:

+ `.aquabot` shows a short introduction
+ `.help` shows a list of all commands

## Requirements
+ python>=3.6.0
