import media
import fresh_tomatoes

# Create a list to store movie instances
movie_list = [];

# Create multiple movie instances
toy_story = media.Movie(
						"Toy Story",
						81,
						"A story of a boy and his toys that come to life",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie(
					"Avatar",
					162,
					"A marine on an alien planet",
					"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					"http://www.youtube.com/watch?v=-9ceBgWV8io")

starwar_2015 = media.Movie(
							"Star War 2015",
						  135,
						  "Visionary director J.J. Abrams brings to life the motion picture event of a generation.",
						  "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
						  "https://www.youtube.com/watch?v=-eYxeRJCYMY")

school_of_rock = media.Movie(
							"School of Rock",
							109,
							"Using rock music to learn",
							"https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
							"https://www.youtube.com/watch?v=LqEszt5wG9I")

ratatouille = media.Movie(
						"Ratatouille",
						115,
						"A rat is a chef in Paris",
						"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
						"https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie(
							"Midnight in Paris",
							100,
							"Going back in time to meet authors",
							"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
							"https://www.youtube.com/watch?v=BYRWfS2s2v4")

# Put the created motive instances into the list
movie_list.append(toy_story)
movie_list.append(avatar)
movie_list.append(starwar_2015)
movie_list.append(school_of_rock)
movie_list.append(ratatouille)
movie_list.append(midnight_in_paris)

# Generate and open the website using the list of movie objects
fresh_tomatoes.open_movies_page(movie_list)

