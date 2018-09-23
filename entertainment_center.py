import fresh_tomatoes
import media

# first Movies
Wings_of_Liberty = media.Movie("StarCraft II: Wings of Liberty",
                               "The storyline of StarCraft II takes place"
                               "four years after StarCraft: Brood War.",
                               "http://wallpaperswide.com/download/starcraft_ii__wings_of_liberty-wallpaper-640x480.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=XZd9n373vf4")
# 2nd movie
Heart_of_the_Swarm = media.Movie("StarCraft II: Heart of the Swarm",
                                 "Heart of the Swarm is a sequel"
                                 "to Wings of Liberty.",
                                 "http://stuffpoint.com/science-fiction/image/348357-science-fiction-starcraft-ii-heart-of-the-swarm-wallpaper.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=MVbeoSPqRs4")
# 3rd movie
Legacy_of_the_Void = media.Movie("StarCraft II: Legacy of the Void",
                                 "Legacy of the Void is a sequel"
                                 "to Heart of the Swarm.",
                                 "https://cdn.wccftech.com/wp-content/uploads/2015/03/StarCraft-II-Legacy-Of-The-Void.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=M_XwzBMTJaM")
# 4th movie
Hearthstone = media.Movie("Hearthstone",
                          "Hearthstone is a free-to-play "
                          "online collectible card video game.",
                          "https://wallpapercave.com/wp/wp1840268.jpg",
                          "https://www.youtube.com/watch?v=vPguoeYTvMI")
# 5th movie
World_of_Warcraft = media.Movie("World of Warcraft",
                                "World of Warcraft (WoW) is a massively "
                                "multiplayer online role-playing game.",
                                "https://images5.alphacoders.com/879/879575.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=jSJr3dXZfcg")
# 6th movie
Diablo_III = media.Movie("Diablo III",
                         "Diablo III is a hack and slash "
                         "action role-playing game (ARPG).",
                         "https://desktopwalls.net/wp-content/uploads/2015/08/Diablo%203%20Reaper%20of%20Souls%20Desktop%20Wallpaper.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=Cb7QJwQ58T0&has_verified=1")  # NOQA

# movie list
movies = [Wings_of_Liberty, Heart_of_the_Swarm,
          Legacy_of_the_Void, Hearthstone,
          World_of_Warcraft, Diablo_III]
# call function
fresh_tomatoes.open_movies_page(movies)
