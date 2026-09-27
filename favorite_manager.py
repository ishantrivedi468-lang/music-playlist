def add_favorite(songs, favorites):
    song = input("Enter song name: ")

    if song in songs:

        if song in favorites:
            print("Song already in favorites!")
        else:
            favorites.append(song)
            print("Added to favorites!")

    else:
        print("Song not found!")


def remove_favorite(favorites):
    song = input("Enter favorite song to remove: ")

    if song in favorites:
        favorites.remove(song)
        print("Removed from favorites!")
    else:
        print("Song not found in favorites!")


def view_favorites(favorites):
    if len(favorites) == 0:
        print("No favorite songs!")
    else:
        print("Favorite Songs:")

        for i in range(len(favorites)):
            print(i + 1, ".", favorites[i])