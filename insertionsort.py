from music_utils import Song

def insertion_sort(songs):
    for i in range(1, len(songs)):
        current_song = songs[i]
        j = i - 1
        
        while j >= 0 and (
            songs[j].rating < current_song.rating or 
            (songs[j].rating == current_song.rating and songs[j].title > current_song.title)):
            
            songs[j + 1] = songs[j]
            j -= 1
        
        songs[j + 1] = current_song

    return songs

songs = Song.generate_random_songs(1000)
ordered = insertion_sort(songs)

for song in ordered:
    print("[", song.rating, "]", song.title, "-", song.artist, "-", song.genre, "-", song.release_date)
