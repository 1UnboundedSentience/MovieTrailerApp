import media
import fresh_tomatoes


shawshank = media.Movie('Shawshank Redemption', 'http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm', 'https://www.youtube.com/watch?v=6hB3S9bIaco')

titanic = media.Movie('Titantic', 'https://titanicsound.files.wordpress.com/2014/11/titanic_movie-hd-1.jpg', 'https://www.youtube.com/watch?v=thrdkT9vE3k')

star_wars_8 = media.Movie('Star Wars 8', 'http://static.srcdn.com/wp-content/uploads/2017/01/star-wars-8-last-jedi.jpg','https://www.youtube.com/watch?v=Yw_rdbY2I1c'
)

print shawshank

movies_list = [shawshank, titanic, star_wars_8]

fresh_tomatoes.open_movies_page( movies_list )