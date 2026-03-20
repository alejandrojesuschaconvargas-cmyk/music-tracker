import csv
from django.core.management.base import BaseCommand
from catalog.models import Artist, Album, Track, Playlist, PlaylistTrack


class Command(BaseCommand):
    help = "Import tracks, artists, albums, and playlists from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        csv_path = options["csv_path"]

        with open(csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                artist_name = (row.get("track_artist") or "Unknown Artist").strip()
                album_title = (row.get("track_album_name") or "Unknown Album").strip()
                track_title = (row.get("track_name") or "Unknown Track").strip()
                playlist_name = (row.get("playlist_name") or "Unknown Playlist").strip()
                playlist_genre = (row.get("playlist_genre") or "Unknown").strip()
                playlist_subgenre = (row.get("playlist_subgenre") or "Unknown").strip()

                popularity = int(float(row.get("track_popularity") or 0))
                duration_ms = int(float(row.get("duration_ms") or 0))
                duration_seconds = duration_ms // 1000

                danceability_value = row.get("danceability")
                energy_value = row.get("energy")

                danceability = float(danceability_value) if danceability_value else None
                energy = float(energy_value) if energy_value else None

                artist, _ = Artist.objects.get_or_create(
                    name=artist_name,
                    defaults={
                        "genre": playlist_genre,
                        "country": "Unknown",
                    }
                )

                album, _ = Album.objects.get_or_create(
                    title=album_title,
                    artist=artist,
                    defaults={
                        "release_year": 2020,
                    }
                )

                track, _ = Track.objects.get_or_create(
                    title=track_title,
                    album=album,
                    artist=artist,
                    defaults={
                        "duration_seconds": duration_seconds,
                        "popularity": popularity,
                        "danceability": danceability,
                        "energy": energy,
                    }
                )

                playlist, _ = Playlist.objects.get_or_create(
                    name=playlist_name,
                    defaults={
                        "genre": playlist_genre,
                        "subgenre": playlist_subgenre,
                    }
                )

                PlaylistTrack.objects.get_or_create(
                    playlist=playlist,
                    track=track,
                )

        self.stdout.write(self.style.SUCCESS("CSV import completed successfully."))