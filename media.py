import webbrowser


# def a class
class Movie:
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # self.title is the name of the movie
        # self.storyline is the brief sum of this movie
        # self.poster_image is the poster
        # self.trailer_youtube_url is the link from youtube
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


"""
def function for opening trailer that when user click
movies,which shows trailer from youtube
"""


def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
