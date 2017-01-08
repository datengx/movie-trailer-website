import webbrowser

class Video():
	"""This class proviced a way to store information of general video"""
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration

class Movie(Video):
	"""This class provides a way to store movie related information"""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	def __init__(self, movie_title, movie_duration, movie_storyline, poster_image, trailer_youtube):
		# Calling initializer of parent
		Video.__init__(self, movie_title, movie_duration)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	