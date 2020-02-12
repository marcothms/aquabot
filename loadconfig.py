"""
Gather all config data into one file,
so all other files can call it from here

loadconfig.py then gets called in aquabot.py
"""

# IMPORTS
import yaml

# Variable Gathering
__avatar__ = "https://i.imgur.com/mskM9dH.png"

try:
    with open("config/config.yml") as file:
        config = yaml.safe_load(file)
    for yml_entry in config:
        __token__ = config[yml_entry]['token']
        __prefix__ = config[yml_entry]['prefix']
except yaml.YAMLError as error:
    print(f"Error while parsing: {error}")

try:
    from config.config import __token__, __prefix__
    from config.cogs import __cogs__
    from config.status import __activity__
    from config.media import __anime_media__, __waifu_media__
except ImportError as error:
    print(f"Error while importing: {error}")
