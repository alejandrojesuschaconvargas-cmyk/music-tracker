from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tracks/", views.track_list, name="track_list"),
    path("tracks/<int:track_id>/", views.track_detail, name="track_detail"),
    path("playlists/", views.playlist_list, name="playlist_list"),
    path("playlists/<int:playlist_id>/", views.playlist_detail, name="playlist_detail"),

    #APIs
    path("api/artists/", views.api_artist_list, name="api_artist_list"),
    path("api/albums/", views.api_album_list, name="api_album_list"),
    path("api/tracks/", views.api_track_list, name="api_track_list"),
    path("api/tracks/<int:track_id>/", views.api_track_detail, name="api_track_detail"),
    path("api/playlists/", views.api_playlist_list, name="api_playlist_list"),
    path("api/playlists/<int:playlist_id>/", views.api_playlist_detail, name="api_playlist_detail"),
]

