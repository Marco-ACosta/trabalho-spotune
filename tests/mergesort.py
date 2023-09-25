from music_utils import Song

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

songs = Song.generate_random_songs(100)
ordered = merge_sort(songs)

for song in ordered:
    print("[", song.rating, "]", song.title, "-", song.artist, "-", song.genre, "-", song.release_date)
