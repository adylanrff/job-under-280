from service.service import Service

class JobService(Service):
    def __init__(self, session, twitter_api):
        super().__init__(session)
    
    