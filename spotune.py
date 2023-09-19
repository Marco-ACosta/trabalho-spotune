
from music_utils import Song

def criar_buckets(songs):
    buckets = []
    for song in songs:
        genre = song.genre.upper()
        
        if genre not in buckets:
            buckets[genre] = []
    
        buckets[genre].append(song)
    return buckets

# def criar_buckets(songs):
#     buckets = []
#     for song in songs:
#         genre = song.genre.upper()
        
#         if genre not in buckets:
#             buckets[genre] = []
    
#         buckets[genre].append(song)
#         # if(len(buckets[genre]) >= 7):
#         #     buckets = quick_sort(buckets)
        
#         # buckets = insertion_sort(buckets)
#     return buckets

# def insertion_sort(buckets, song):
#     for i in range(len(buckets[genre])):
#         if(song.rating < buckets[genre][i].rating):
#             buckets[genre].insert(i, song)
        
# def quick_sort(buckets):
    
#     return None

# def insertion_sort(buckets):
    
#     return None

# def sort_genres(bucket):
#     new_bucket = []
#     for genre in bucket:
        

#     return None

songs = Song.generate_random_songs(100)
for song in songs:
    print("[", song.rating, "]", song.title, "-", song.artist, "-", song.genre, "-", song.release_date)

buckets = criar_buckets(songs)

print("a")

# sort_genres(buckets)

# for genre in buckets:
#     print(f'{genre}:')
#     for i in range(len(genre)):
#         print(f'\t{buckets[genre][i]}')
