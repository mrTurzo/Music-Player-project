# music_player.py

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist} - {self.duration} minutes"


class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return f"Album: {self.title} by {self.artist} - {len(self.songs)} songs"

    def list_songs(self):
        for song in self.songs:
            print(song)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def __str__(self):
        return f"Playlist: {self.name} - {len(self.songs)} songs"

    def list_songs(self):
        for song in self.songs:
            print(song)


class MusicPlayer:
    def __init__(self):
        self.songs = []
        self.albums = []
        self.playlists = []

    def add_song(self, song):
        self.songs.append(song)

    def add_album(self, album):
        self.albums.append(album)

    def add_playlist(self, playlist):
        self.playlists.append(playlist)

    def play_song(self, song):
        print(f"Playing: {song}")

    def list_all_songs(self):
        for song in self.songs:
            print(song)

    def list_all_albums(self):
        for album in self.albums:
            print(album)
            album.list_songs()

    def list_all_playlists(self):
        for playlist in self.playlists:
            print(playlist)
            playlist.list_songs()


if __name__ == "__main__":
    # Create some songs
    song1 = Song("Song One", "Artist One", 3.5)
    song2 = Song("Song Two", "Artist Two", 4.0)
    song3 = Song("Song Three", "Artist One", 5.0)

    # Create an album and add songs to it
    album = Album("Album One", "Artist One")
    album.add_song(song1)
    album.add_song(song3)

    # Create a playlist and add songs to it
    playlist = Playlist("My Playlist")
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)

    # Create a music player and add songs, albums, and playlists
    player = MusicPlayer()
    player.add_song(song1)
    player.add_song(song2)
    player.add_song(song3)
    player.add_album(album)
    player.add_playlist(playlist)

    # List all songs, albums, and playlists
    print("\nAll Songs:")
    player.list_all_songs()

    print("\nAll Albums:")
    player.list_all_albums()

    print("\nAll Playlists:")
    player.list_all_playlists()

    # Play a song
    player.play_song(song1)
