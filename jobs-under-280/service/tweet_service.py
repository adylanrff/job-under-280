from service.service import Service

class TweetService(Service):
    def __init__(self, session, twitter_api):
        super().__init__(session)
        self.twitter_api = twitter_api
    
