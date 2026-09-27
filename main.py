from song_manager import (
    add_song,
    remove_song,
    view_songs,
    search_song
)

from playlist_manager import (
    create_playlist,
    delete_playlist,
    add_to_playlist,
    remove_from_playlist,
    view_playlists,
    shuffle_playlist
)

from favorite_manager import (
    add_favorite,
    remove_favorite,
    view_favorites
)

from storage import load_data, save_data


data = load_data()

songs = data["songs"]
playlists = data["playlists"]
favorites = data["favorites"]

while True:

    print("================================")
    print("      MUSIC PLAYLIST MANAGER")
    print("================================")

    print("1. Add Song")
    print("2. Remove Song")
    print("3. View All Songs")
    print("4. Search Song")
    print("5. Create Playlist")
    print("6. Delete Playlist")
    print("7. Add Song to Playlist")
    print("8. Remove Song from Playlist")
    print("9. View Playlists")
    print("10. Shuffle Playlist")
    print("11. Add Favorite")
    print("12. Remove Favorite")
    print("13. View Favorites")
    print("14. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        add_song(songs)

    elif choice == "2":
        remove_song(songs)

    elif choice == "3":
        view_songs(songs)

    elif choice == "4":
        search_song(songs)

    elif choice == "5":
        create_playlist(playlists)

    elif choice == "6":
        delete_playlist(playlists)

    elif choice == "7":
        add_to_playlist(songs, playlists)

    elif choice == "8":
        remove_from_playlist(playlists)

    elif choice == "9":
        view_playlists(playlists)

    elif choice == "10":
        shuffle_playlist(playlists)

    elif choice == "11":
        add_favorite(songs, favorites)

    elif choice == "12":
        remove_favorite(favorites)

    elif choice == "13":
        view_favorites(favorites)

    elif choice == "14":
        save_data(songs, playlists, favorites)

        print("Thank you for using Music Playlist Manager!")

        break

    else:
        print("Invalid choice!")