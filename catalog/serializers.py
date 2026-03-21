from rest_framework import serializers
from .models import Artist, Album, Track, Playlist, PlaylistTrack


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name", "genre", "country"]


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = ["id", "title", "release_year", "artist"]


class TrackSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Track
        fields = [
            "id",
            "title",
            "duration_seconds",
            "popularity",
            "danceability",
            "energy",
            "artist",
            "album",
        ]


class PlaylistTrackSerializer(serializers.ModelSerializer):
    track = TrackSerializer(read_only=True)

    class Meta:
        model = PlaylistTrack
        fields = ["id", "track"]


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ["id", "name", "genre", "subgenre", "created_at"]


class PlaylistDetailSerializer(serializers.ModelSerializer):
    playlist_tracks = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = ["id", "name", "genre", "subgenre", "created_at", "playlist_tracks"]

    def get_playlist_tracks(self, obj):
        playlist_tracks = PlaylistTrack.objects.select_related(
            "track", "track__artist", "track__album"
        ).filter(playlist=obj)
        return PlaylistTrackSerializer(playlist_tracks, many=True).data