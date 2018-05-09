import webbrowser


# Creates a class called Movie
class Movie():

    #This sets the movies attributes
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #This opens the browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
