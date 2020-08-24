"""
Gather all config data into one file,
so all other files can call it from here

loadconfig.py then gets called in aquabot.py
"""

# IMPORTS
import yaml

__avatar__ = "https://i.redd.it/0uajctrps9u41.jpg"

# Import from yaml
try:
    with open("config/config.yml") as file:
        config = yaml.safe_load(file)

        __token__ = config['token']
        __prefix__ = config['prefix']

except yaml.YAMLError as error:
    print(f"Error while parsing: {error}")
except FileNotFoundError as error:
    print(f"Error, please create a config file: {error}")

# Import from *.py in config/ and data/
try:
    from config.cogs import __cogs__

    from data.media import __media_anime__, __media_girl__
    from data.memes import __memes_list__
except ImportError as error:
    print(f"Error while importing: {error}")
