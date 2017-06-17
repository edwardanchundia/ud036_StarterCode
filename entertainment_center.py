import fresh_tomatoes
import media

# Five hundred days of Summer Movie:
# movie title, storyline, poster image and movie trailer
five_hundred_days = media.Movie(
    "500 Days of Summer",
    "A man's 500 days with Summer.",
    "https://upload.wikimedia.org/wikipedia/en/d/d1/Five_hundred_days_of_summer.jpg",  # NOQA
    "https://www.youtube.com/watch?v=PsD0NpFSADM"  # NOQA
)
# Marley and Me Movie:
# movie title, storyline, poster image and movie trailer
marley_and_me = media.Movie(
    "Marley & Me",
    "Life with Marley.",
    "https://upload.wikimedia.org/wikipedia/en/1/16/MarleyPoster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=0UMMGNxg1Lg"  # NOQA
)
# Pursuit of Happyness Movie:
# movie title, storyline, poster image and movie trailer
pursuit_of_happyness = media.Movie(
    "The Pursuit of Happyness",
    "When the pursuit toward happyness becomes hard but rewarding.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",  # NOQA
    "https://www.youtube.com/watch?v=89Kq8SDyvfg"  # NOQA
)
# Armageddon Movie:
# movie title, storyline, poster image and movie trailer
armageddon = media.Movie(
    "Armageddon",
    "A group of hard working men work to save "
    "the world by destroying a astroid.",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Armageddon-poster06.jpg",  # NOQA
    "https://www.youtube.com/watch?v=kg_jH47u480"  # NOQA
)
# Midnigh in Paris Movie:
# movie title, storyline, poster image and movie trailer
midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "A man journey in the streets of paris.",
    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=FAfR8omt-CY"  # NOQA
)
# Iron Man Movie:
# movie title, storyline, poster image and movie trailer
iron_man = media.Movie(
    "Iron Man",
    "Tony Stark is destine to save the world as Iron Man.",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",  # NOQA
    "https://www.youtube.com/watch?v=8hYlB38asDY"  # NOQA
)

# Set the movies in array to get passed to open_movie_page
movies = [
    five_hundred_days,
    marley_and_me,
    pursuit_of_happyness,
    armageddon,
    midnight_in_paris,
    iron_man
]
# Opens html file in browser using fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
