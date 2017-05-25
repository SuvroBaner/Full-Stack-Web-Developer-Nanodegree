import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

boyhood = media.Movie("Boyhood",
                      "The life of Mason, from early childhood to his arrival at college",
                      "https://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg",
                      "https://www.youtube.com/watch?v=Ys-mbHXyWX4")


school_of_rock = media.Movie("School of Rock",
                             "Using Rock Music to Learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=28iEsXRAM9I")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=-SWvAo51ems")

movies = [toy_story, avatar, boyhood, school_of_rock, ratatouille, midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)

#print(boyhood.title)
#print(boyhood.storyline)
#boyhood.show_trailer()
#boyhood.show_poster()

#print(toy_story.title)
#print(toy_story.storyline)
#toy_story.show_trailer()
#toy_story.show_poster()

#print(avatar.title)
#print(avatar.storyline)
#avatar.show_trailer()
#avatar.show_poster()

