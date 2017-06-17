import fresh_tomatoes
import media

five_hundred_days = media.Movie("500 Days of Summer",
                        "A man's 500 days with Summer.",
                        "https://upload.wikimedia.org/wikipedia/en/d/d1/Five_hundred_days_of_summer.jpg",
                        "https://www.youtube.com/watch?v=PsD0NpFSADM")
marley_and_me = media.Movie("Marley & Me",
                     "Life with Marley.",
                     "https://upload.wikimedia.org/wikipedia/en/1/16/MarleyPoster.jpg",
                     "https://www.youtube.com/watch?v=0UMMGNxg1Lg")
pursuit_of_happyness = media.Movie("The Pursuit of Happyness",
                             "When the pursuit toward happyness becomes hard but rewarding.",
                             "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                             "https://www.youtube.com/watch?v=89Kq8SDyvfg")
armageddon = media.Movie("Armageddon",
                          "A group of hard working men work to save the world by destroying a astroid.",
                          "https://upload.wikimedia.org/wikipedia/en/f/fc/Armageddon-poster06.jpg",
                          "https://www.youtube.com/watch?v=kg_jH47u480")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "A man journey in the streets of paris.", 
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
iron_man = media.Movie("Iron Man",
                        "Tony Stark is destine to save the world as Iron Man.",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://www.youtube.com/watch?v=8hYlB38asDY")

movies = [five_hundred_days, marley_and_me, pursuit_of_happyness, armageddon, midnight_in_paris, iron_man]
fresh_tomatoes.open_movies_page(movies)