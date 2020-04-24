"""
Gather all config data into one file,
so all other files can call it from here

loadconfig.py then gets called in aquabot.py
"""

# IMPORTS
import yaml

# Variable Gathering
__avatar_old__ = "https://i.imgur.com/mskM9dH.png"
__avatar__ = "https://i.redd.it/0uajctrps9u41.jpg"

try:
    with open("config/config.yml") as file:
        config = yaml.safe_load(file)

        __token__ = config['token']
        __prefix__ = config['prefix']

except yaml.YAMLError as error:
    print(f"Error while parsing: {error}")
except FileNotFoundError as error:
    print(f"Error, please create a config file: {error}")

try:
    from config.cogs import __cogs__
    from config.status import __activity__
    from config.media import __media_anime__, __media_girl__
except ImportError as error:
    print(f"Error while importing: {error}")
