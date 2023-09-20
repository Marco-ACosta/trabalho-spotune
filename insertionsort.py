from music_utils import Song

def insertion_sort(songs):
    # Percorre a lista de músicas a partir do segundo elemento (índice 1).
    for i in range(1, len(songs)):
        current_song = songs[i]
        j = i - 1
        
        # Enquanto 'j' for maior ou igual a 0 e a música à esquerda tiver uma classificação maior
        # ou, em caso de empate na classificação, um título alfabeticamente maior,
        # movemos a música à esquerda uma posição para a direita.
        while j >= 0 and (songs[j].rating < current_song.rating or (songs[j].rating == current_song.rating and songs[j].title > current_song.title)):
            songs[j + 1] = songs[j]
            j -= 1
        
        # Coloca a música atual na posição correta da lista ordenada.
        songs[j + 1] = current_song
    
    return songs


songs = Song.generate_random_songs(100)
ordered = insertion_sort(songs)

for song in ordered:
    print("[", song.rating, "]", song.title, "-", song.artist, "-", song.genre, "-", song.release_date)
