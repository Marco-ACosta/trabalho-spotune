from music_utils import Song

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    for _ in range(len(left) + len(right)):
        if left_index < len(left) and right_index < len(right):
            
            if left[left_index].rating > right[right_index].rating:
                merged.append(left[left_index])
                left_index += 1
            
            elif left[left_index].rating == right[right_index].rating:
            
                if left[left_index].title < right[right_index].title:
                    merged.append(left[left_index])
                    left_index += 1
                
                else:
                    merged.append(right[right_index])
                    right_index += 1

            else:
                merged.append(right[right_index])
                right_index += 1

        elif left_index < len(left):
            merged.append(left[left_index])
            left_index += 1
        
        else:
            merged.append(right[right_index])
            right_index += 1
    
    return merged

def merge_sort(songs):
    if len(songs) <= 1:
        return songs

    mid = len(songs) // 2

    left_half = songs[:mid]
    right_half = songs[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


songs = Song.generate_random_songs(1000)
ordered = merge_sort(songs)

for song in ordered:
    print("[", song.rating, "]", song.title, "-", song.artist, "-", song.genre, "-", song.release_date)
