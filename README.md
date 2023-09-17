
# Music Time Machine

The Music Time Machine is a Python project that allows you to travel back in time and create Spotify playlists with the top songs from a specific year. It scrapes Billboard's Hot 100 charts for a given year and creates a private Spotify playlist with those songs.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a Spotify Developer account and have created a Spotify App. You will need the Client ID and Client Secret.
- You have Python 3.x installed.
- You have the required Python packages installed, which can be installed using `pip`:

```shell
pip install requests beautifulsoup4 spotipy python-dotenv

```

## Installation
To install and run this project, follow these steps:

Clone this repository:

```shell
git clone ht[README.md](README.md)tps://github.com/yourusername/music-time-machine.git
cd music-time-machine
```


Create a .env file in the project directory and add your Spotify App credentials:
env
```shell
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your[]()_client_secret
SPOTIPY_REDIRECT_URI=http://example.com
```


Run the Python script:
```shell
python music_time_machine.py
```

## Usage
- Run the script and input the year you want to travel to when prompted.

- The script will scrape Billboard's Hot 100 charts for that year and search for each song on Spotify.

- A private Spotify playlist named <year> Billboard 100 will be created, and the top 100 songs from that year will be added to the playlist.

- Enjoy your time-traveling music playlist!

