import csv

with open("/home/ale/Desktop/music_tracker/data/spotify_small_tracks.csv", newline="", encoding="utf-8") as f:
    reader= csv.DictReader(f)
    print(reader.fieldnames)