from music_utils import Song
import time

songs = Song.generate_random_songs(1000)
inicio = time.time()
songs_order = sorted(songs, key=lambda song: song.rating, reverse=True)
fim = time.time()
for song in songs_order:
    print(song)

print(f"Tempo gasto: {fim - inicio}")
