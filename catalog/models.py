from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, default="Unknown")
    country = models.CharField(max_length=100, default="Unknown")

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_year = models.IntegerField(default=2020)

    def __str__(self):
        return f"{self.title} - {self.artist.name}"

class Track(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    duration_seconds = models.IntegerField()
    popularity = models.IntegerField()
    danceability = models.FloatField(null = True, blank = True)
    energy = models.FloatField(null = True, blank = True)

    def __str__(self):
        return f"{self.title} - {self.artist.name}"

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, default="Unknown")
    subgenre = models.CharField(max_length=100, default="Unknown")
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class PlaylistTrack(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["playlist", "track"], name="unique_playlist_track")
        ]
    
    def __str__(self):
        return f"{self.playlist.name} - {self.track.title}"