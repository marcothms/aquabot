"""
Gather all config data into one file

loadconfig.py then gets called in aquabot.py
"""

from config.cogs import __cogs__

try:
    from config.config import __token__, __prefix__
except ImportError as e:
    print(f"Error while importing: {e}")
