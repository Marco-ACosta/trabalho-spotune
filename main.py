from music_utils import Song

'''
TRABALHO SPOTUNE
- Marco Antônio
- Raisson Souza

Esse é o arquivo principal do trabalho.
'''

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    for _ in range(len(left) + len(right)):
        # Verifica se ainda há elementos em ambas as listas para mesclar.
        if left_index < len(left) and right_index < len(right):
            # Compara os elementos com base no rating.
            if left[left_index].rating > right[right_index].rating:
                # Se o elemento na lista esquerda tiver um rating maior, adiciona no array merged.
                merged.append(left[left_index])
                left_index += 1
            
            # Se o rating for igual, compara os títulos dos elementos.
            elif left[left_index].rating == right[right_index].rating:
                # Se o title da musica no array da esquerda for menor, adiciona no array merged.
                if left[left_index].title < right[right_index].title:
                    merged.append(left[left_index])
                    left_index += 1
                
                else:
                    # Se o title da musica no array da direita for menor, adiciona no array merged.
                    merged.append(right[right_index])
                    right_index += 1

            else:
                # Se o elemento na lista direita tiver um rating maior, adiciona no array merged.
                merged.append(right[right_index])
                right_index += 1

        # Se não houver mais elementos no array da esquerda, adiciona os restantes do array da direita no array merged.
        elif left_index < len(left):
            merged.append(left[left_index])
            left_index += 1
        # Se não houver mais elementos no array da direita, adiciona os restantes do array da esquerda no array merged.
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Retorna o array merged mesclado e ordenados.
    return merged

def merge_sort(songs):
    # Verifica se a lista de músicas tem um tamanho menor ou igual a 1 se tiver quer dizer que não tem mais o que dividir, então retorna.
    if len(songs) <= 1:
        return songs

    mid = len(songs) // 2

    # Divide a lista em duas metades: left_half e right_half.
    left_half = songs[:mid]
    right_half = songs[mid:]

    # Chama recursivamente merge_sort, até que o tamanho do array seja menor ou igual a 1.
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Chama a função de merge para combinar as duas listas de forma ordenada.
    return merge(left_sorted, right_sorted)

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

def create_buckets(songs = []):
    buckets = []
    genres_c = 0
    genres_dic = {}
    genres_list = []

    for song in songs:
        genre = song.genre.upper()
        
        if genre not in genres_dic:
            buckets.append({'genre': genre, 'songs': []})
            genres_dic[genre] = genres_c
            genres_list.append(genre)
            genres_c += 1
    
        buckets[genres_dic[genre]]['songs'].append(song)
        
    return buckets, genres_list

def sort_genres(buckets = [], genres = []):
    '''Ordena os gêneros de músicas'''

    new_bucket = []
    for i in range(1, len(genres)):
        current_genre = genres[i]
        j = i - 1
        while j >= 0 and genres[j] < current_genre:
            genres[j + 1] = genres[j]
            j -= 1
        genres[j + 1] = current_genre
    
    for genre in genres:
        for bucket in buckets:
            if bucket['genre'] == genre:
                new_bucket.append({ 'genre': genre, 'songs': bucket['songs'] })
                break
    
    return new_bucket

songs = Song.generate_random_songs(10)

buckets, genres = create_buckets(songs)
ordered_buckets = sort_genres(buckets, genres)

for bucket in ordered_buckets:
    if(len(bucket['songs']) > 7):
        bucket['songs'] = insertion_sort(bucket['songs'])
    else:
        bucket['songs'] = merge_sort(bucket['songs'])

for bucket in ordered_buckets:
    print(f"\nGenêro: {bucket['genre'].capitalize()}\t\tQuantidade de músicas: {len(bucket['songs'])}")
    for song in bucket['songs']:
        print(f"\t[{song.rating}]", song.title, "-", song.artist, "-", song.genre, "-", song.release_date)
