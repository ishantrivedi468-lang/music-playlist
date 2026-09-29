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

<img width="1397" height="586" alt="image" src="https://github.com/user-attachments/assets/1aa6fe20-759d-462c-ad44-3971d8a4a315" />

---

### 3. Search for a Song

Choose **Search Song** and enter the name of the song.

The program checks the song collection and displays whether the song was found.

<img width="597" height="467" alt="image" src="https://github.com/user-attachments/assets/9b3b0c0f-248c-405f-9d12-f0f11323accc" />

---

### 4. Remove a Song

Choose **Remove Song** and enter the name of the song you want to remove.

If the song exists, it will be removed from the collection.

<img width="562" height="447" alt="image" src="https://github.com/user-attachments/assets/9a4316ae-fbde-4689-9159-7e1593352371" />

---

### 5. Create a Playlist

Choose **Create Playlist** and enter a name for your new playlist.

The playlist will be created and can then be managed using the playlist options.

<img width="547" height="452" alt="image" src="https://github.com/user-attachments/assets/9b692b5c-b213-477f-9bd7-0499577e91db" />


---



### 6. Add a Song to a Playlist

Choose **Add Song to Playlist**.

Select the required playlist and song. The song will be added to that playlist.

---

<img width="457" height="490" alt="image" src="https://github.com/user-attachments/assets/e7a90b8b-6da5-4a43-9a80-3f2b05b64073" />

### 7. Remove a Song from a Playlist

Choose **Remove Song from Playlist**.

Select the playlist and song you want to remove.

The song will be removed from that playlist without removing it from the main song collection.

<img width="502" height="475" alt="image" src="https://github.com/user-attachments/assets/2e1bd985-1e1e-4671-b4d5-c372f0e1ea10" />


---

### 8. View Playlists

Choose **View Playlists** to display the playlists created by the user and their songs.


<img width="421" height="542" alt="image" src="https://github.com/user-attachments/assets/3df935fa-4db7-44fa-b260-e73e8fa5f26b" />


---

### 9. Shuffle a Playlist

Choose **Shuffle Playlist** and select the playlist you want to shuffle.

The songs in that playlist will be rearranged into a shuffled order.


<img width="391" height="451" alt="image" src="https://github.com/user-attachments/assets/561f40c3-984d-4de7-b68c-52e4f6f3370d" />

---

### 10. Delete a Playlist

Choose **Delete Playlist** and enter the playlist you want to delete.

The selected playlist will be removed from the playlist collection.

<img width="467" height="446" alt="image" src="https://github.com/user-attachments/assets/c14b6651-a71c-4741-b1c5-4c58f0811577" />

---


### 11. Add a Favorite

Choose **Add Favorite** and select a song from the available songs.

The selected song will be added to the favorites list.

<img width="495" height="455" alt="image" src="https://github.com/user-attachments/assets/7529e720-dd15-4052-8bc6-e3138254bf23" />

---


### 12. View Favorites

Choose **View Favorites** to display all songs currently marked as favorites.

<img width="402" height="475" alt="image" src="https://github.com/user-attachments/assets/fd1657df-7b5a-412f-b11c-3960eeef16ae" />

---




### 13. Remove a Favorite

Choose **Remove Favorite** to remove a song from the favorites list.

The original song remains available in the main song collection.

<img width="452" height="447" alt="image" src="https://github.com/user-attachments/assets/9414d992-6902-4325-9d83-dc617a62aefa" />


---

### 14. Exit

Choose **Exit** to close the application.

Before exiting, the program saves the current songs, playlists, and favorites to `data.json`.

<img width="566" height="427" alt="image" src="https://github.com/user-attachments/assets/f325dc4f-6d9c-43d5-8e56-fef84fc14f81" />

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
