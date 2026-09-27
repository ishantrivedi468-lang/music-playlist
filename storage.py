import json


def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)

    return data


def save_data(songs, playlists, favorites):
    data = {
        "songs": songs,
        "playlists": playlists,
        "favorites": favorites
    }

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)