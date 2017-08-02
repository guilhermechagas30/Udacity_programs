import media
import fresh_tomatoes

toy_story = media.Movie("toy Story", "A story about a boy",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on alien planet",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)

#toy_story.show_trailer()

stranger_things = media.Movie("Stranger Things","Stories from the upside down",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEzMDAxOTUyMV5BMl5BanBnXkFtZTgwNzAxMzYzOTE@._V1_.jpg",
                              "https://www.youtube.com/watch?v=vgS2L7WPIO4")

print(stranger_things.title)

stranger_things.show_trailer()

movies = [toy_story, avatar, stranger_things]
fresh_tomatoes.open_movies_page(movies)
