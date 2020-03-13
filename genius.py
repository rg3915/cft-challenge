import os
from dotenv import load_dotenv
from lyricsgenius import Genius
from typing import List

load_dotenv()


def get_popularity_songs(artist_name: str, max_songs: int, sort="popularity"):
    genius = Genius(os.environ["TOKEN"])
    artist = genius.search_artist(artist_name, max_songs=max_songs, sort=sort)
    return artist.songs
