import media
import fresh_tomatoes


# Toy Story movie: movie title, storyline, poster image, movie trailer
toy_story = media.Movie("Toy Story",
                        "Toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Avatar movie: movie title, storyline, poster image, movie trailer
avatar = media.Movie("Avatar",
                     "The story of unobtanium",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

# School of Rock movie: movie title, storyline, poster image, movie trailer
school_of_rock = media.Movie("School_of_Rock",
                             "The story of a school rockstar",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# Ratatouille movie: movie title, storyline, poster image, movie trailer
ratatouille = media.Movie("Ratatouille",
                          "The story of a rat who turns into a chef",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=uVeNEbh3A4U")

# Midnight in Paris movie: movie title, storyline, poster image, movie trailer
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Sounds like a romantic movie with a message",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

# Hunger Games movie: movie title, storyline, poster image, movie trailer
hunger_games = media.Movie("The Hunger Games",
                           "The story of some hungry people playing"
                           " silly games",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

# Set of movies that will be passed to the fresh_tomatoes.py file for
# rendering on the web-page
movies = [toy_story,
          avatar,
          school_of_rock,
          ratatouille,
          midnight_in_paris,
          hunger_games]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
