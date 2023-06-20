import spotipy
from spotipy.oauth2 import SpotifyOAuth
import tkinter as tk
from tkinter import messagebox
import webbrowser

# Set up Spotify API credentials
client_id = '<your client id here>'
client_secret = '<your client secret here>'
redirect_uri = 'http://localhost:8888/callback'

# Set up authentication flow
scope = 'playlist-modify-public user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Get the user's playlists
playlists = sp.current_user_playlists()

# Create the GUI window
window = tk.Tk()
window.title("Spotify Playlist Automation")
window.geometry("500x300")

# Create a label for playlist selection
playlist_label = tk.Label(window, text="Select a playlist:")
playlist_label.pack(pady=10)

# Create a listbox to display the playlist names
playlist_listbox = tk.Listbox(window, selectmode=tk.SINGLE)
for playlist in playlists['items']:
    playlist_listbox.insert(tk.END, playlist['name'])
playlist_listbox.pack(pady=10)

# Create a frame to display song information
song_frame = tk.Frame(window)

# Create a label for song name
song_name_label = tk.Label(song_frame, text="", font=("Helvetica", 16))
song_name_label.pack(pady=5)

# Create a label for artist name
artist_label = tk.Label(song_frame, text="", font=("Helvetica", 12))
artist_label.pack()

# Initialize the current song index
current_song_index = 0

# Initialize the all_liked_songs variable as a global list
all_liked_songs = []

# Function to update the song information
def update_song_info():
    global all_liked_songs
    song = all_liked_songs[current_song_index]['track']
    song_name_label.config(text=song['name'])
    artist_label.config(text=song['artists'][0]['name'])

# Function to open Spotify web player for the current song
def open_spotify_web():
    song = all_liked_songs[current_song_index]['track']
    url = song['external_urls']['spotify']
    webbrowser.open(url)

# Function to add the current song to the selected playlist
def add_to_playlist():
    selected_playlist_index = playlist_listbox.curselection()
    if len(selected_playlist_index) == 0:
        messagebox.showinfo("Error", "Please select a playlist.")
        return

    selected_playlist_id = playlists['items'][selected_playlist_index[0]]['id']

    # Add the song to the selected playlist
    track_uri = all_liked_songs[current_song_index]['track']['uri']
    sp.playlist_add_items(selected_playlist_id, [track_uri])
    messagebox.showinfo("Success", "Song added to the playlist.")

# Function to handle playlist selection
def select_playlist():
    selected_playlist_index = playlist_listbox.curselection()
    if len(selected_playlist_index) == 0:
        messagebox.showinfo("Error", "Please select a playlist.")
        return

    playlist_label.pack_forget()
    playlist_listbox.pack_forget()

    global current_song_index, all_liked_songs
    current_song_index = 0
    all_liked_songs = sp.current_user_saved_tracks(limit=50)['items']

    if len(all_liked_songs) == 0:
        messagebox.showinfo("Info", "You have no liked songs.")
        window.destroy()
    else:
        update_song_info()
        song_frame.pack()

# Function to skip to the next song
def next_song():
    global current_song_index
    current_song_index += 1
    if current_song_index >= len(all_liked_songs):
        current_song_index = 0
    update_song_info()
    update_background_color()

# Function to go back to the playlist selection
def go_back():
    song_frame.pack_forget()
    back_button.pack_forget()
    playlist_label.pack()
    playlist_listbox.pack()


back_button = tk.Button(song_frame, text="Back", command=go_back)

# Set up the GUI layout

# Create the buttons frame
buttons_frame = tk.Frame(window)

# Create the Previous button
previous_button = tk.Button(buttons_frame, text="Previous", command=next_song)
previous_button.pack(side=tk.LEFT, padx=5)

# Create the No (X) button
no_button = tk.Button(buttons_frame, text="✕", fg="red", font=("Helvetica", 12), command=next_song)
no_button.pack(side=tk.LEFT, padx=5)

# Create the Yes (checkmark) button
yes_button = tk.Button(buttons_frame, text="✓", fg="green", font=("Helvetica", 12), command=add_to_playlist)
yes_button.pack(side=tk.LEFT, padx=5)

# Pack the buttons frame at the bottom with padding
buttons_frame.pack(side=tk.BOTTOM, pady=10)

# Function to update the background color based on the song's tempo
def update_background_color():
    song = all_liked_songs[current_song_index]['track']
    tempo = song['tempo'] if 'tempo' in song else 0
    normalized_tempo = (tempo - 60) / 140  # Normalize tempo between 60 and 200 to a range of 0 to 1

    # Convert the normalized tempo to an RGB color
    red = int(normalized_tempo * 255)
    green = 0
    blue = 255 - int(normalized_tempo * 255)

    # Convert RGB values to hexadecimal format
    color_hex = f"#{red:02x}{green:02x}{blue:02x}"

    window.configure(background=color_hex)

# Bind select playlist function to the Enter key
window.bind('<Return>', lambda event: select_playlist())

# Start the GUI event loop
window.mainloop()