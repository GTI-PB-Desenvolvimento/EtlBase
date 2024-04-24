import psycopg as pg
import requests as rq
from sqlalchemy import create_engine, Engine


class Etl:
    def connection(self, dsn) -> pg.Connection:
        return pg.connect(dsn)

    def create_engine(self, con) -> Engine:
        return create_engine(
            'postgresql+psycopg://',
            creator=con
        )

class RequestsBaseExtraction(Etl):
    def __init__(self, dsn_db):
        self.engine = self.create_engine(
            self.connection(dsn_db)
        )
        self.rq = rq.session()

