# Playlist Automator (for Spotify)

Playlist Automator is a Python script designed to automate the creation and management of Spotify playlists based on user-defined criteria. Leveraging the Spotipy library, it interacts seamlessly with the Spotify Web API to perform tasks such as retrieving user playlists, searching for tracks, and creating new playlists.

## Features

- **User Authentication**: Securely authenticate with Spotify using OAuth, ensuring user data privacy.
- **Playlist Retrieval**: Fetch and display existing user playlists.
- **Track Search**: Search for tracks based on various parameters like artist, album, or track name.
- **Playlist Creation**: Create new playlists and add selected tracks to them.

## Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed on your system.
- **Spotipy Library**: Install Spotipy, a lightweight Python library for the Spotify Web API.
- **Spotify Developer Account**: Register an application to obtain your `client_id` and `client_secret`.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sahilgagvani/Playlist-Automator.git
   ```


2. **Install Dependencies**:
   ```bash
   pip install spotipy
   ```


3. **Set Up Spotify Credentials**:
   - Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new application.
   - Note down your `client_id` and `client_secret`.
   - Set up a redirect URI (e.g., `http://localhost:8888/callback`).

4. **Configure Environment Variables**:
   ```bash
   export SPOTIPY_CLIENT_ID='your_client_id'
   export SPOTIPY_CLIENT_SECRET='your_client_secret'
   export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
   ```


## Usage

1. **Run the Script**:
   ```bash
   python spotify-playlist-automator.py
   ```


2. **Authenticate**:
   - Upon running the script, a browser window will prompt you to log in to your Spotify account and grant the necessary permissions.

3. **Follow On-Screen Instructions**:
   - The script will guide you through retrieving your playlists, searching for tracks, and creating new playlists based on your inputs.

## Notes

- **API Rate Limits**: Be mindful of Spotify's rate limits when making API requests. Excessive requests in a short time may lead to temporary restrictions.
- **Error Handling**: The script includes basic error handling. For more robust error management, consider enhancing the existing mechanisms.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

For more information on Spotipy and its capabilities, refer to the [Spotipy Documentation](https://spotipy.readthedocs.io/).
