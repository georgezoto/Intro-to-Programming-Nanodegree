import media
import fresh_tomatoes

fast_and_furious = media.Movie('The Fast and the Furious',
                                "The film follows undercover cop Brian O'Conner, who is tasked with stopping a group of unknown hijackers using high-performance racecars to hijack 18-wheelers.",
                                'https://upload.wikimedia.org/wikipedia/en/5/54/Fast_and_the_furious_poster.jpg',
                                'http://www.youtube.com/watch?v=ZsJz2TJAPjw&t=0m9s')

#print(fast_and_furious.storyline)
#fast_and_furious.show_trailer()

friends = media.Movie('Friends',
                                "Friends is an American television sitcom, created by David Crane and Marta Kauffman, which aired on NBC from September 22, 1994, to May 6, 2004, lasting ten seasons. With an ensemble cast starring Jennifer Aniston, Courteney Cox, Lisa Kudrow, Matt LeBlanc, Matthew Perry and David Schwimmer, the show revolves around six 20-30 something friends living in Manhattan.",
                                'https://www.justwatch.com/images/poster/501626/s592',
                                'https://www.youtube.com/watch?v=TgP8v60X23c')

#print('\n'+friends.storyline)
movies = [fast_and_furious, friends]

fresh_tomatoes.open_movies_page(movies)
