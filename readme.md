# 🎵 Music Playlist Manager

A simple **Python-based command-line application** for managing songs, playlists, and favorite songs.

The project uses a menu-driven interface where users can add, remove, search, and view songs, create and manage playlists, shuffle playlists, and manage favorite songs.

Application data is stored in a **JSON file**, allowing the saved songs, playlists, and favorites to remain available after the program is closed and opened again.

---

## 📌 Features

### 🎵 Song Management

* Add a new song
* Remove a song
* View all songs
* Search for a song
* Prevent duplicate songs

### 📂 Playlist Management

* Create a playlist
* Delete a playlist
* Add songs to a playlist
* Remove songs from a playlist
* View all playlists
* Shuffle songs in a playlist

### ⭐ Favorite Management

* Add songs to favorites
* Remove songs from favorites
* View favorite songs

### 💾 Data Storage

* Store songs, playlists, and favorites in `data.json`
* Load saved data when the program starts
* Save updated data when the program exits

---

## 🛠️ Technologies Used

* **Python**
* **JSON**
* **VS Code**

The project uses Python modules to separate different parts of the application, making the code easier to organize and understand.

---

## 📁 Project Structure

```text
music-playlist/
│
├── main.py
├── song_manager.py
├── playlist_manager.py
├── favorite_manager.py
├── storage.py
├── data.json
├── readme.md
└── statement.md
```

### File Description

| File                  | Description                                                         |
| --------------------- | ------------------------------------------------------------------- |
| `main.py`             | Runs the main menu and connects all modules                         |
| `song_manager.py`     | Handles adding, removing, viewing, and searching songs              |
| `playlist_manager.py` | Handles playlist creation, deletion, song management, and shuffling |
| `favorite_manager.py` | Handles adding, removing, and viewing favorite songs                |
| `storage.py`          | Handles loading and saving application data                         |
| `data.json`           | Stores songs, playlists, and favorites                              |
| `statement.md`        | Contains the project statement/details                              |

The repository currently follows this modular structure, with `main.py` importing functions from the song, playlist, favorite, and storage modules.

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/ishantrivedi468-lang/music-playlist.git
```

### 2. Open the Project

Open the project folder in **VS Code** or another Python-compatible editor.

### 3. Run the Program

Run:

```bash
python main.py
```

The Music Playlist Manager menu will appear in the terminal.

---

## 🎮 Main Menu

```text
================================
      MUSIC PLAYLIST MANAGER
================================

1. Add Song
2. Remove Song
3. View All Songs
4. Search Song
5. Create Playlist
6. Delete Playlist
7. Add Song to Playlist
8. Remove Song from Playlist
9. View Playlists
10. Shuffle Playlist
11. Add Favorite
12. Remove Favorite
13. View Favorites
14. Exit

Enter your choice:
```

The menu and its 14 options are implemented in `main.py`.

---

## 📖 How to Use

### 1. Add a Song

Choose **Add Song** from the main menu.

Enter the song name when prompted. The song will be added to the collection.

If the song already exists, the program will notify you instead of adding a duplicate.

<img width="1412" height="591" alt="image" src="https://github.com/user-attachments/assets/b7e215b2-68bb-4ae4-8f11-5563c8c5670a" />


---

### 2. View All Songs

Choose **View All Songs** to display all songs currently stored in the application.

The songs are displayed as a numbered list.

---

### 3. Search for a Song

Choose **Search Song** and enter the name of the song.

The program checks the song collection and displays whether the song was found.

---

### 4. Remove a Song

Choose **Remove Song** and enter the name of the song you want to remove.

If the song exists, it will be removed from the collection.

---

### 5. Create a Playlist

Choose **Create Playlist** and enter a name for your new playlist.

The playlist will be created and can then be managed using the playlist options.

---

### 6. Delete a Playlist

Choose **Delete Playlist** and enter the playlist you want to delete.

The selected playlist will be removed from the playlist collection.

---

### 7. Add a Song to a Playlist

Choose **Add Song to Playlist**.

Select the required playlist and song. The song will be added to that playlist.

---

### 8. Remove a Song from a Playlist

Choose **Remove Song from Playlist**.

Select the playlist and song you want to remove.

The song will be removed from that playlist without removing it from the main song collection.

---

### 9. View Playlists

Choose **View Playlists** to display the playlists created by the user and their songs.

---

### 10. Shuffle a Playlist

Choose **Shuffle Playlist** and select the playlist you want to shuffle.

The songs in that playlist will be rearranged into a shuffled order.

---

### 11. Add a Favorite

Choose **Add Favorite** and select a song from the available songs.

The selected song will be added to the favorites list.

---

### 12. Remove a Favorite

Choose **Remove Favorite** to remove a song from the favorites list.

The original song remains available in the main song collection.

---

### 13. View Favorites

Choose **View Favorites** to display all songs currently marked as favorites.

---

### 14. Exit

Choose **Exit** to close the application.

Before exiting, the program saves the current songs, playlists, and favorites to `data.json`.

---

## 💾 Data Storage

The project uses `data.json` to store application data.

The stored information includes:

```text
Songs
Playlists
Favorites
```

When the program starts, the saved information is loaded from the JSON file.

When the user exits the program, the latest information is saved back to the file.

This allows the application data to remain available between different program sessions.

---

## 🔄 Basic Program Flow

```text
              Run main.py
                   │
                   ▼
              Load data
             from JSON
                   │
                   ▼
              Main Menu
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
     Songs      Playlists    Favorites
       │           │           │
       └───────────┼───────────┘
                   ▼
              Update Data
                   │
                   ▼
             Save to JSON
                   │
                   ▼
                  Exit
```

---

## 🧩 Project Architecture

The project is divided into separate Python modules:

```text
main.py
   │
   ├── song_manager.py
   │
   ├── playlist_manager.py
   │
   ├── favorite_manager.py
   │
   └── storage.py
             │
             ▼
          data.json
```

This modular approach keeps song management, playlist management, favorite management, and data storage separated instead of placing the entire program in one file.

---

## 🎯 Learning Objectives

This project demonstrates the use of:

* Python functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Modules and imports
* User input
* JSON file handling
* Basic data management
* Menu-driven programming
* Modular code organization

---

## 🚀 Future Improvements

Some possible improvements for future versions include:

* 🎧 Play actual audio files
* 🔊 Add music controls such as play, pause, and stop
* 🔎 Improve search with partial song-name matching
* 🎨 Create a graphical user interface
* 💿 Add artist and album information
* 📊 Add playlist statistics
* 🔐 Add user profiles
* ☁️ Add cloud-based data storage

---

## 👨‍💻 Author

**Ishan Trivedi**

Computer Science student interested in Python, AI/ML, and software development.

---

## ⭐ Project

If you find this project useful or interesting, feel free to explore the repository and give it a star.

**Repository:**
https://github.com/ishantrivedi468-lang/music-playlist
