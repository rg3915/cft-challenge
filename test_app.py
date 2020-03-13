import unittest
from collections import namedtuple
from unittest import mock
from app import create_app

Song = namedtuple("Song", ["title", "year", "album"])


class ArtistTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()

    @mock.patch("app.get_popularity_songs")
    def test_get_artist_popularity_songs(self, song_mocked):
        data = [
            Song(
                title="Nothing Else Matters",
                year="1991-08-12",
                album="Metallica"
            )
        ]
        song_mocked.return_value = data

        response = self.client.get("/artist/Metallica")
        self.assertListEqual(
            list(response.get_json()),
            [
                {
                    'title': data[0].title,
                    'year': data[0].year,
                    'album': data[0].album,
                }
            ]
        )

    def tearDown(self) -> None:
        self.context.pop()
