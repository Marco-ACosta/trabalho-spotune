import random
title_words = ["Love", "Sunset", "Dream", "Ocean", "Sky", "Heart", "Moon", "Stars"]
artist_names = ["HarmonyWeaver", "MelodyForge", "RhythmCraft", "MusicMaker", "TuneMaster"]
genres = ["Pop", "Rock", "Electronic", "Hip Hop", "Jazz", "Classical"]
class Song:
    def __init__(self, title, artist, genre, release_date, rating):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.release_date = release_date
        self.rating = rating
    def __str__(self):
        return f"{self.title} by {self.artist}" # modifique-me :)
    @staticmethod
    def generate_random_songs(num_songs = 1):
        random_songs = []
        for _ in range(num_songs):
            title = random.choice(title_words) + " " + random.choice(title_words)
            artist = random.choice(artist_names)
            genre = random.choice(genres)
            release_date = f"{random.randint(2000, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            rating = round(random.uniform(0, 5), 1)
            random_songs.append(Song(title, artist, genre, release_date, rating))
        return random_songs