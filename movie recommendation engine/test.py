class movie:
    def __init__(self, title, genre_set):
        self.title = title
        self.genre = genre_set

    def __str__(self):
        genre_string = ",".join(self.genre)
        return f"{self.title} ({genre_string})"
class recommendation_engine:
    def __init__(self):
        self.movie_database = []
    def add_movies(self, movie_object):
        self.movie_database.append(movie_object)
    def calculate_similarity(self, movie1, movie2):
        common = movie1.genre.intersection(movie2.genre)
        similarity_score = len(common) / len(movie1.genre.union(movie2.genre)) if len(movie1.genre.union(movie2.genre)) > 0 else 0
        return similarity_score 
    
    def get_recommendations(self, target_movie):
        best_score = -1
        best_match = None
        for movie in self.movie_database:
            if movie.title == target_movie.title:
                continue
            score = self.calculate_similarity(target_movie, movie)
            if score > best_score:
                best_score = score
                best_match = movie
        return best_score, best_match


movie1 = movie("Interception", {"Action", "Thriller", "Mystery", })
movie2 = movie("Conjuting", {"Horror", "Mystery", })
movie3 = movie("Interstellar", {"Sci-Fi", "Space", "Drama"})
movie4 = movie("The Dark Knight", {"Action", "Thriller", "Crime"})

print(movie1)
print(movie2)
print(movie3)
print(movie4)

engine = recommendation_engine()

engine.add_movies(movie1)
engine.add_movies(movie2)
engine.add_movies(movie3)
engine.add_movies(movie4)

score, recommended_movie = engine.get_recommendations(movie1)

print(f"Because you watched: {movie1.title}")
print(f"You should watch: {recommended_movie.title} (Similarity Score: {score:.2f})")