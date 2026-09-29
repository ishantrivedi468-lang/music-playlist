# Music Playlist Manager

## Overview

The program can be run from `main.py`. The other Python files contain different functions, which are imported as modules in `main.py`.

Music Playlist Manager is a simple Python-based project that allows users to manage their songs, playlists, and favorite songs.

The project uses a menu-driven system where the user can add, remove, search and view songs. Users can also create playlists, add or remove songs from playlists, shuffle playlists, and manage favorite songs.

The data is stored in a JSON file so that the information is available even after closing and reopening the program.

---

## Features

The main features of the project are:

- Add a new song
- Remove a song
- View all songs
- Search for a song
- Create a playlist
- Delete a playlist
- Add songs to a playlist
- Remove songs from a playlist
- View playlists
- Shuffle a playlist
- Add songs to favorites
- Remove songs from favorites
- View favorite songs
- Store data using JSON file

---

## Technologies Used

- Python
- JSON
- VS Code

---

## Project Structure

```text
MusicPlaylistManager/

│
├── main.py
├── song_manager.py
├── playlist_manager.py
├── favorite_manager.py
├── storage.py
├── data.json
└── README.md



## How to Use

### 1. Run the Program

Run the `main.py` file to start the Music Playlist Manager.

The main menu will be displayed on the screen.

---

### 2. Add a Song

Select the **Add Song** option from the main menu.

Enter the required song details when prompted. The song will then be added to the song collection.

**Screenshot:**
*Add screenshot of adding a song here.*

---

### 3. View All Songs

Select **View All Songs** to display all songs currently stored in the application.

**Screenshot:**
*Add screenshot of the songs list here.*

---

### 4. Search for a Song

Select **Search Song** and enter the song name or required search information.

The program will display the matching song if it is available.

**Screenshot:**
*Add screenshot of the search feature here.*

---

### 5. Create a Playlist

Select **Create Playlist** and enter a name for the new playlist.

The playlist will be created and can be managed from the playlist options.

**Screenshot:**
*Add screenshot of creating a playlist here.*

---

### 6. Add Songs to a Playlist

Select **Add Song to Playlist**.

Choose the required playlist and song. The selected song will be added to the playlist.

**Screenshot:**
*Add screenshot of adding a song to a playlist here.*

---

### 7. View Playlists

Select **View Playlists** to see the playlists created by the user along with their songs.

**Screenshot:**
*Add screenshot of viewing playlists here.*

---

### 8. Shuffle a Playlist

Select **Shuffle Playlist** and choose the playlist you want to shuffle.

The songs in the selected playlist will be arranged in a shuffled order.

**Screenshot:**
*Add screenshot of shuffled playlist here.*

---

### 9. Manage Favorite Songs

The **Favorites** option allows users to:

* Add songs to favorites
* Remove songs from favorites
* View favorite songs

**Screenshot:**
*Add screenshot of the favorites section here.*

---

### 10. Remove Songs or Playlists

The application also provides options to remove songs from the main collection and delete playlists that are no longer required.

**Screenshot:**
*Add screenshot of the remove/delete operation here.*

---

### 11. Data Storage

The project uses `data.json` to store application data.

This allows songs, playlists, and favorite information to remain available even after the program is closed and opened again.

**Screenshot:**
*Add screenshot of `data.json` here.*















