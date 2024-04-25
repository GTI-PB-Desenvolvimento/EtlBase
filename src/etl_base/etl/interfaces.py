import requests as rq

from ..db import pg_engine, PGConfig


class RequestsBaseExtraction:
    def __init__(self, db_config: PGConfig):
        self.engine = pg_engine(db_config)
        self.rq = rq.session()

