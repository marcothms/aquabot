"""
Gather all config data into one file

loadconfig.py then gets called in aquabot.py
"""

__avatar__ = "https://i.imgur.com/mskM9dH.png"

from config.cogs import __cogs__

from config.status import __activity__

try:
    from config.config import __token__, __prefix__
except ImportError as e:
    print(f"Error while importing: {e}")
