import media
import fresh_tomatoes

fast_and_furious = media.Movie('The Fast and the Furious',
                                "The film follows undercover cop Brian O'Conner, who is tasked with stopping a group of unknown hijackers using high-performance racecars to hijack 18-wheelers.",
                                'https://upload.wikimedia.org/wikipedia/en/5/54/Fast_and_the_furious_poster.jpg',
                                'http://www.youtube.com/watch?v=ZsJz2TJAPjw&t=0m9s',
                                'June 22, 2001',
                                '106 minutes')

#print(fast_and_furious.storyline)
#fast_and_furious.play_media()

friends = media.TVShow('Friends',
                        "Friends is an American television sitcom, created by David Crane and Marta Kauffman, which aired on NBC from September 22, 1994, to May 6, 2004, lasting ten seasons. With an ensemble cast starring Jennifer Aniston, Courteney Cox, Lisa Kudrow, Matt LeBlanc, Matthew Perry and David Schwimmer, the show revolves around six 20-30 something friends living in Manhattan.",
                        'https://www.justwatch.com/images/poster/501626/s592',
                        'https://www.youtube.com/watch?v=TgP8v60X23c',
                        'September 22, 1994',
                        'May 6, 2004',
                        10,
                        236)

#print('\n'+friends.storyline)
movies = [fast_and_furious, friends]

fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print('doc', media.Movie.__doc__)
#print('name', media.Movie.__name__)
#print('module', media.Movie.__module__)
##print(media.Movie.__defaults__)
##print(media.Movie.__code__)
##print(media.Movie.__globals__)
#print('dict', media.Movie.__dict__)
##print(media.Movie.__closure__)
