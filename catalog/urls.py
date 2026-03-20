from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tracks/", views.track_list, name="track_list"),
    path("tracks/<int:track_id>/", views.track_detail, name="track_detail"),
    path("playlists/", views.playlist_list, name="playlist_list"),
    path("playlists/<int:playlist_id>/", views.playlist_detail, name="playlist_detail"),
]

