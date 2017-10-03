import webbrowser


class Movie():
    ''' This class is used to store movie related information '''
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # class variable

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        ''' Constructor method to initialize the movie related info. '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        ''' This function will open the movie trailer on a browser. '''
        webbrowser.open(self.trailer_youtube_url)
