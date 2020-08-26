"""
Gather all media data into one file,
so all other files can call it from here

"""

try:
    from data.media import __media_anime__, __media_girl__
    from data.memes import __memes_list__
except ImportError as error:
    print(f"Error while importing: {error}")
