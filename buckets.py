from music_utils import Song

def sort_genres(buckets = [], genres = []):
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

def create_buckets(songs = []):
    buckets = []
    genres_c = 0
    genres_dic = {}
    genres_list = []

    for song in songs:
        genre = song.genre.upper()
        
        if genre not in genres_dic:
            buckets.append({ 'genre': genre, 'songs': [] })
            genres_dic[genre] = genres_c
            genres_list.append(genre)
            genres_c += 1
    
        buckets[genres_dic[genre]]['songs'].append(song)
        
    return buckets, genres_list

songs = Song.generate_random_songs(10)

buckets, genres = create_buckets(songs)
new_buckets = sort_genres(buckets, genres)
for bucket in new_buckets:
    print(f"Genêro: {bucket['genre']}\t\tQuantidade de músicas: {len(bucket['songs'])}")
    for song in bucket['songs']:
        print(f"\t[{song.rating}]", song.title, "-", song.artist, "-", song.genre, "-", song.release_date)
