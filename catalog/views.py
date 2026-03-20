from django.shortcuts import render, get_object_or_404
from .models import Artist, Album, Track, Playlist, PlaylistTrack


def home(request):
    context = {
        "artist_count": Artist.objects.count(),
        "album_count": Album.objects.count(),
        "track_count": Track.objects.count(),
        "playlist_count": Playlist.objects.count(),
    }
    return render(request, "catalog/home.html", context)


def track_list(request):
    tracks = Track.objects.select_related("artist", "album").all().order_by("title")
    query = request.GET.get("q")

    if query:
        tracks = tracks.filter(title__icontains=query)

    context = {
        "tracks": tracks[:100],
        "query": query or "",
    }
    return render(request, "catalog/track_list.html", context)


def track_detail(request, track_id):
    track = get_object_or_404(
        Track.objects.select_related("artist", "album"),
        id=track_id
    )

    context = {
        "track": track,
    }
    return render(request, "catalog/track_detail.html", context)


def playlist_list(request):
    playlists = Playlist.objects.all().order_by("name")

    context = {
        "playlists": playlists[:100],
    }
    return render(request, "catalog/playlist_list.html", context)


def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    playlist_tracks = PlaylistTrack.objects.select_related(
        "track", "track__artist", "track__album"
    ).filter(playlist=playlist)

    context = {
        "playlist": playlist,
        "playlist_tracks": playlist_tracks,
    }
    return render(request, "catalog/playlist_detail.html", context)

