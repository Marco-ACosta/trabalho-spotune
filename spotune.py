
from music_utils import Song

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

# def insertion_sort(songs):
#     pass

# def compare(song1, song2):
#     # se os ratings forem diferentes, compare-os em ordem decrescente
#     if song1.rating != song2.rating:
#         return song2.rating - song1.rating
#     # se os ratings forem iguais, compare os titles em ordem alfabética decrescente
#     else:
#         return -1 * (song1.title > song2.title) + 1 * (song1.title < song2.title)

# def mergesort(songs, inicio, fim):
#     # se o inicio for maior ou igual ao fim, retorne sem fazer nada
#     if inicio >= fim:
#         return

#     # se o inicio for igual ao fim menos um, compare os dois elementos da sublista
#     if inicio == fim - 1:
#         if compare(songs[inicio], songs[fim]) > 0:
#             # troque-os de lugar se necessário
#             songs[inicio], songs[fim] = songs[fim], songs[inicio]
#         return

#     # se o inicio for menor que o fim menos um, divida a sublista em duas metades
#     meio = (inicio + fim) // 2
#     # aplique a função recursivamente a cada metade
#     mergesort(songs, inicio, meio)
#     mergesort(songs, meio + 1, fim)

#     # crie uma lista vazia para armazenar o resultado da fusão
#     resultado = []
#     # use dois ponteiros para percorrer as duas metades ordenadas
#     i = inicio
#     j = meio + 1
#     while i <= meio and j <= fim:
#         # compare os elementos apontados pela função de comparação
#         if compare(songs[i], songs[j]) <= 0:
#             # adicione o menor elemento à lista de resultado
#             resultado.append(songs[i])
#             # avance o ponteiro correspondente
#             i += 1
#         else:
#             # adicione o menor elemento à lista de resultado
#             resultado.append(songs[j])
#             # avance o ponteiro correspondente
#             j += 1

#     # adicione os elementos restantes da outra metade à lista de resultado
#     if i <= meio:
#         resultado.extend(songs[i:meio + 1])
#     if j <= fim:
#         resultado.extend(songs[j:fim + 1])

#     # copie os elementos da lista de resultado para a lista original
#     for k in range(inicio, fim + 1):
#         songs[k] = resultado[k - inicio]

def sort_genres(buckets = [], genres = []):
    new_bucket = []
    
    # reverter ordem (alfabetico contratio)
    for i in range(len(genres)):
        if i <= len(genres) and i+1 < len(genres):
            if genres[i] > genres[i + 1]:
                genres[i], genres[i+1] = genres[i+1], genres[i]
        for j in range(0, i):
            if j - 1 >= 0:
                if genres[j] < genres[j - 1]:
                    genres[j], genres[j-1] = genres[j-1], genres[j]
    
    for i, genre in enumerate(genres):
        new_bucket.append({'genre': genre, 'songs': buckets[i]['songs']})

    return new_bucket

songs = Song.generate_random_songs(100)
for song in songs:
    print("[", song.rating, "]", song.title, "-", song.artist, "-", song.genre, "-", song.release_date)

buckets, genres = create_buckets(songs)

buckets = sort_genres(buckets, genres)

print("a")


# for genre in buckets:
#     print(f'{genre}:')
#     for i in range(len(genre)):
#         print(f'\t{buckets[genre][i]}')

