"""
Gather all config data into one file,
so all other files can call it from here

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

# Load cogs activated from the start
try:
    from config.cogs import __cogs__
except ImportError as error:
    print(f"Error while importing: {error}")
