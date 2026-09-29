import json
import os

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")


def load_data():
    try:
        with open(FILE, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    return {
        "songs": data.get("songs", []),
        "playlists": data.get("playlists", {}),
        "favorites": data.get("favorites", []),
    }


def save_data(songs, playlists, favorites):
    data = {
        "songs": songs,
        "playlists": playlists,
        "favorites": favorites
    }

    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)
