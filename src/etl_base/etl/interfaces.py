import requests as rq

from ..db import pg_engine


class RequestsBaseExtraction:
    def __init__(self):
        self.engine = pg_engine()
        self.rq = rq.session()

