from flask import Flask, jsonify
from genius import get_popularity_songs


def artist(name):
    # artist route
    songs = get_popularity_songs(name, max_songs=10)
    content = [
        {
            "title": song.title,
            "year": song.year,
            "album": song.album
        }
        for song in songs
    ]
    return jsonify(content)


def create_app():
    app = Flask(__name__)
    app.add_url_rule("/artist/<name>", 'artist', artist)

    return app
