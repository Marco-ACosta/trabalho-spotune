from music_utils import Song
import time

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

def merge_sort_data(songs):
    # Verifica se a lista de músicas tem um tamanho menor ou igual a 1 se tiver quer dizer que não tem mais o que dividir, então retorna.
    if len(songs) <= 1:
        return songs

    mid = len(songs) // 2

    # Divide a lista em duas metades: left_half e right_half.
    left_half = songs[:mid]
    right_half = songs[mid:]

    # Chama recursivamente merge_sort, até que o tamanho do array seja menor ou igual a 1.
    left_sorted = merge_sort_data(left_half)
    right_sorted = merge_sort_data(right_half)

    # Chama a função de merge para combinar as duas listas de forma ordenada.
    return merge_data(left_sorted, right_sorted)

def merge_data(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    for _ in range(len(left) + len(right)):
        # Verifica se ainda há elementos em ambas as listas para mesclar.
        if left_index < len(left) and right_index < len(right):
            # Compara os elementos com base no rating.
            if left[left_index].release_date > right[right_index].release_date:
                # Se o elemento na lista esquerda tiver um rating maior, adiciona no array merged.
                merged.append(left[left_index])
                left_index += 1
            
            # Se o release_date for igual, compara os ratings dos elementos.
            elif left[left_index].release_date == right[right_index].release_date:
                # Se o rating da musica no array da esquerda for menor, adiciona no array merged.
                if left[left_index].rating > right[right_index].rating:
                    merged.append(left[left_index])
                    left_index += 1
                
                # Compara se o rating for igual, compara os títulos dos elementos.
                elif left[left_index].rating == right[right_index].rating:
                    # Se o title da musica no array da direita for menor, adiciona no array merged.
                    if left[left_index].title < right[right_index].title:
                        merged.append(left[left_index])
                        left_index += 1
                    
                    else:
                        # Se o title da musica no array da direita for menor, adiciona no array merged.
                        merged.append(right[right_index])
                        right_index += 1
                
                else:
                    # Se o rating da musica no array da direita for menor, adiciona no array merged.
                    merged.append(right[right_index])
                    right_index += 1

            else:
                # Se o elemento na lista direita tiver um release_date maior, adiciona no array merged.
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

def insertion_sort_data(songs):
    # Percorre a lista de músicas a partir do segundo elemento (índice 1).
    for i in range(1, len(songs)):
        current_song = songs[i]
        j = i - 1
        
        # Enquanto 'j' for maior ou igual a 0 e a música à esquerda tiver uma data de lançamento mais recente
        # ou, em caso de empate na data, tiver uma classificação menor ou um título alfabeticamente menor,
        # movemos a música à esquerda uma posição para a direita.
        while j >= 0 and (
            songs[j].release_date < current_song.release_date or 
            (songs[j].release_date == current_song.release_date and songs[j].rating < current_song.rating) or
            (songs[j].release_date == current_song.release_date and songs[j].rating == current_song.rating and songs[j].title < current_song.title)
        ):
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

        # Verifica se o gênero ainda não está no dicionário de gêneros
        if genre not in genres_dic:
            # Se não estiver, cria um novo bucket para esse gênero
            buckets.append({'genre': genre, 'songs': []})
            # Mapeia o gênero para o índice do bucket
            genres_dic[genre] = genres_c
            # Adiciona o gênero à lista de gêneros
            genres_list.append(genre)
            # Incrementa o contador de gêneros
            genres_c += 1
    
        # Adiciona a música ao bucket correspondente ao seu gênero
        buckets[genres_dic[genre]]['songs'].append(song)
        
    # Retorna a lista de buckets e a lista de gêneros
    return buckets, genres_list

def sort_genres(buckets = [], genres = []):
    new_bucket = [] 

    # Ordena a lista de gêneros em ordem alfabética reversa
    for i in range(1, len(genres)):
        current_genre = genres[i]
        j = i - 1

        # Enquanto j for maior ou igual a 0 e o gênero anterior for maior que o gênero atual
        while j >= 0 and genres[j] < current_genre:
            # Move o gênero anterior uma posição à frente na lista, deslocando para a direita
            genres[j + 1] = genres[j]
            j -= 1

        # Quando na posição correta insere nessa posição
        genres[j + 1] = current_genre

    
    for genre in genres:
        # Procura o bucket correspondente ao gênero na lista de buckets
        for bucket in buckets:
            if bucket['genre'] == genre:
                # Adiciona o bucket encontrado à lista de buckets ordenados
                new_bucket.append({'genre': genre, 'songs': bucket['songs']})
                break
    
    # Retorna a lista de buckets ordenados
    return new_bucket

def main():
    songs = Song.generate_random_songs(100000)
    buckets, genres = create_buckets(songs)
    ordered_buckets = sort_genres(buckets, genres)

    while True:
        print('\t\t### Spotune ###\n\tComo deseja ordenar suas músicas?\n')
        try:
            opc = int(input('\t[ 1 ] Ano de Lançamento\n\t[ 2 ] Avaliação\n>>> '))
        except:
            opc = 4

        if opc == 1:
            inicio = time.time()
            for bucket in ordered_buckets:
                if (len(bucket['songs']) > 7):
                    bucket['songs'] = merge_sort_data(bucket['songs'])
                else:
                    bucket['songs'] = insertion_sort_data(bucket['songs'])
            fim = time.time()
            break

        elif opc == 2:
            inicio = time.time()
            for bucket in ordered_buckets:
                if (len(bucket['songs']) > 7):
                    bucket['songs'] = merge_sort(bucket['songs'])
                else:
                    bucket['songs'] = insertion_sort(bucket['songs'])
            fim = time.time()
            break

        else:
            print('Opção inválida, digite uma opção válida.\n')

    for bucket in ordered_buckets:
        print(f"Genêro: {bucket['genre'].capitalize()}\t\tQuantidade de músicas: {len(bucket['songs'])}")
        for song in bucket['songs']:
            print(f"\t[{song.rating}]", song.title, "-", song.artist, "-", song.genre, "-", song.release_date)

    print(f"Tempo gasto: {fim - inicio}")

main()
