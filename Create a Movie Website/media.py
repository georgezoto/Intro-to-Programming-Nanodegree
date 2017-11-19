import webbrowser

class Media():
    '''This class provides a way to store media related information'''
    VALID_RATINGS = []

    def __init__(self, title, storyline, media_image_url, media_video_url, release_date):
        self.title = title
        self.storyline = storyline
        self.media_image_url = media_image_url
        self.media_video_url = media_video_url
        self.release_date = release_date

    def play_media(self):
        '''
        Open a web browser and play the media video url associated with this instance.

        Args:
            self which is an instance of class Media

        Returns:
            New browser playing the video url

        Raises:
            None
        '''
        webbrowser.open(self.media_video_url)

class Movie(Media):
    '''This class provides a way to store movie related information, inherited from Media'''
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, storyline, movie_image_url, movie_video_url, release_date, running_time):
        Media.__init__(self, title, storyline, movie_image_url, movie_video_url, release_date)
        self.running_time = running_time

class TVShow(Media):
    '''This class provides a way to store tv show related information, inherited from Media'''
    VALID_RATINGS = ['TV-Y', 'TV-Y7', 'TV-Y7-FV', 'TV-G', 'TV-PG', 'TV-14', 'TV-MA']

    def __init__(self, title, storyline, tvshow_image_url, tvshow_video_url, release_date, final_date, seasons, episodes):
        Media.__init__(self, title, storyline, tvshow_image_url, tvshow_video_url, release_date)
        self.final_date = final_date
        self.seasons = seasons
        self.episodes = episodes
