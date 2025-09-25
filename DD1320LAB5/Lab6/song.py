class Song:
    def __init__(self, trackid, songid, artistname, title):
        self.trackid = trackid
        self.songid = songid
        self.artist = artistname
        self.title = title

    def __str__(self):
        return f"{self.title} by {self.artist}"

    def __lt__(self, other):
        return self.artistname < other.artistname