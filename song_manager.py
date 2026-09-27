def add_song(songs):
    song = input("Enter song name: ")

    if song in songs:
        print("Song already exists!")
    else:
        songs.append(song)
        print("Song added successfully!")


def remove_song(songs):
    song = input("Enter song name to remove: ")

    if song in songs:
        songs.remove(song)
        print("Song removed!")
    else:
        print("Song not found!")


def view_songs(songs):
    if len(songs) == 0:
        print("No songs available!")
    else:
        print("Your Songs:")

        for i in range(len(songs)):
            print(i + 1, ".", songs[i])


def search_song(songs):
    name = input("Enter song name: ")

    if name in songs:
        print("Song found!")
    else:
        print("Song not found!")