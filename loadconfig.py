"""
Gather all config data into one file

loadconfig.py then gets called in aquabot.py
"""

__avatar__ = "https://i.imgur.com/mskM9dH.png"

try:
    # TODO Maybe use yaml for token and prefix!
    from config.config import __token__, __prefix__
    from config.cogs import __cogs__
    from config.status import __activity__
    from config.media import __anime_media__, __waifu_media__
except ImportError as error:
    print(f"Error while importing: {error}")
