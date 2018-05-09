import media
import fresh_tomatoes

# Favorite Movies To Be Displayed In Browser
jurassic_world = media.Movie("Jurassic World", "A new theme park, built on "
                                               "the original site of "
                                               "Jurassic Park, creates a "
                                               "genetically modified hybrid "
                                               "dinosaur, which escapes "
                                               "containment and goes on a "
                                               "killing spree.",
                             "https://ia.media-imdb.com/images/M"
                             "/MV5BNWEyNTE0YTEtY2FkMi00MmY3LTg4MWMtODdjYjRkNGM"
                             "4ZTZhXkEyXkFqcGdeQXVyMzI0NDc4ODY@._V1_SY1000_CR0"
                             ",0,631,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=RFinNxS5KN4")

forrest_gump = media.Movie("Forrest Gump",
                           "The presidencies of Kennedy and Johnson, "
                           "Vietnam, Watergate, and other " 
                           "history unfold through the perspective of an "
                           "Alabama man with an IQ of 75.",
                           "https://ia.media-imdb.com/images/M"
                           "/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU"
                           "1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR1,0"
                           ",182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

finding_nemo = media.Movie("Finding Nemo",
                           "After his son is captured in the Great Barrier "
                           "Reef and taken to Sydney, a timid clownfish sets "
                           "out on a journey to bring him home.",
                           "https://ia.media-imdb.com/images/M/MV5BZjMxYzBiNjU"
                           "tZDliNC00MDAyLTg3N2QtOWNjNmNhZGQzNDg5XkEyXkFqcGdeQ"
                           "XVyNjE2MjQwNjc@._V1_.jpg",
                           "https://www.youtube.com/watch?v=3JnKU9Stmyw")

the_hurt_locker = media.Movie("The Hurt Locker",
                              "During the Iraq War, a Sergeant recently assig"
                              "ned to an army bomb squad is put at odds with "
                              "his squad mates due to his maverick way of han"
                              "dling his work.",
                              "https://ia.media-imdb.com/images/M/MV5BNzEwNzQ1"
                              "NjczM15BMl5BanBnXkFtZTcwNTk3MTE1Mg@@._V1_.jpg",
                              "https://www.youtube.com/watch?v=oa6RZgUMRz0")

the_dark_knight = media.Movie("The Dark Knight",
                              "When the menace known as the Joker emerges from"
                              " his mysterious past, he wreaks havoc and chaos"
                              " on the people of Gotham. The Dark Knight must "
                              "accept one of the greatest psychological an"
                              "d physical tests of his ability to fight"
                              " injustice.",
                              "https://ia.media-imdb.com/images/M/MV5BMTMxNTMw"
                              "ODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000"
                              "_CR0,0,675,1000_AL_.jpg",
                              "https://www.youtube.com/watch?v=kmJLuwP3MbY")

boyhood = media.Movie("Boyhood",
                      "The life of Mason, from early childhood to his arrival"
                      " at college.",
                      "https://ia.media-imdb.com/images/M/MV5BMTYzNDc2MDc0N15"
                      "BMl5BanBnXkFtZTgwOTcwMDQ5MTE@._V1_SY1000_CR0,0,675,10"
                      "00_AL_.jpg",
                      "https://www.youtube.com/watch?v=oNC3NYWh1vI")

# Array of movies
movies = [jurassic_world, forrest_gump, finding_nemo, the_hurt_locker,
          the_dark_knight, boyhood]
# Opens movies in browser
fresh_tomatoes.open_movies_page(movies)
