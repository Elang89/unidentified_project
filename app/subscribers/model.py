import datetime

from app.database import DB


class Subscriber(object): 

    def __init__(self, name):
        self.name = name
        self.created_at = datetime.datetime.utcnow()