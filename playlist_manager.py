import random


def create_playlist(playlists):
    name = input("Enter playlist name: ")

    if name in playlists:
        print("Playlist already exists!")
    else:
        playlists[name] = []
        print("Playlist created!")


def delete_playlist(playlists):
    name = input("Enter playlist name to delete: ")

    if name in playlists:
        del playlists[name]
        print("Playlist deleted!")
    else:
        print("Playlist not found!")


def add_to_playlist(songs, playlists):
    name = input("Enter playlist name: ")

    if name in playlists:
        song = input("Enter song name: ")

        if song in songs:

            if song in playlists[name]:
                print("Song already exists in playlist!")
            else:
                playlists[name].append(song)
                print("Song added to playlist!")

        else:
            print("Song not found!")

    else:
        print("Playlist not found!")


def remove_from_playlist(playlists):
    name = input("Enter playlist name: ")

    if name in playlists:
        song = input("Enter song name to remove: ")

        if song in playlists[name]:
            playlists[name].remove(song)
            print("Song removed from playlist!")
        else:
            print("Song not found in playlist!")

    else:
        print("Playlist not found!")


def view_playlists(playlists):
    if len(playlists) == 0:
        print("No playlists available!")
    else:
        for name in playlists:
            print("\nPlaylist:", name)

            if len(playlists[name]) == 0:
                print("No songs in playlist!")
            else:
                for i in range(len(playlists[name])):
                    print(i + 1, ".", playlists[name][i])


def shuffle_playlist(playlists):
    name = input("Enter playlist name: ")

    if name in playlists:
        random.shuffle(playlists[name])
        print("Playlist shuffled!")
    else:
        print("Playlist not found!")