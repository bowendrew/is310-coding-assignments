favorite_movies = [
    {"name": "Jurassic Park", "release_year": 1993},
    {"name": "Titanic", "release_year": 1997},
    {"name": "Finding Nemo", "release_year": 2003},
    {"name": "Cars", "release_year": 2006},
    {"name": "Black Panther", "release_year": 2018}
]

def check_movie(movie):
    if movie["release_year"] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movie["name"]
    
recent_movies = []

for movie in favorite_movies:
    returned_movie = check_movie(movie)

    if returned_movie is not None:
        recent_movies.append(returned_movie)

print(recent_movies)