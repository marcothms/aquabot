![Avatar](img/avatar.png)

AquaBot
=======

[![discordpy](https://img.shields.io/badge/discordpy-Core-blue)](https://github.com/Rapptz/discord.py)
[![Discord Server](https://img.shields.io/badge/Support-Discord%20Server-blue.svg)](https://discordapp.com/invite/HbYfyJT)

This bot is my first personal project so expect some minor (or bigger) problems
here and there.
Also note that this bot is still in its very early stages, so there is no
guaranty that all features work!

Support and report requests are handled via Discord (Link above).

Installation - Docker
---------------------

`WIP!`

+ Clone this repository with `git clne https://github.com/CramMK/aquabot`

+ Create a `config/config.py`, using the `config/config_example.py` as a
guideline

+ Launch the Container

Installation - pip
------------------

+ Clone this repository with `git clone https://github.com/CramMK/aquabot`

+ **OPTIONAL:** A virtual environment can be created at this point

+ Use `pip install --user -r requirements.txt` to install all dependencies
needed for the bot

+ Create a `config/config.py`, using the `config/config_example.py` as a
guideline

+ Finally, run `python aquabot`

Commands
------

The following commands assume that `.` is your default prefix.

There are currently two command, which help the user to naviagte the bot's
commands:

+ `.aquabot` shows a short introduction
+ `.help` shows a list of all commands (A custom help message is WIP)

Config
------

To use the bot you need to add a `config/config.py` file. For reference, see
`config/config_example.py`.

Requirements
------------

+ python>=3.6.0
