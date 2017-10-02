import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "Toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)
#toy_story.show_trailer()

avatar = media.Movie("Avatar",
                     "The story of unobtanium",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School_of_Rock",
                             "The story of a school rockstar",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille",
                          "The story of a rat who turns into a chef",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=uVeNEbh3A4U")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "Sounds like a romantic movie with a message",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("The Hunger Games",
                           "The story of some hungry people playing silly games",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)

