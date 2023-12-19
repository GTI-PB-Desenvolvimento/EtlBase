import psycopg as pg
from sqlalchemy import create_engine, Engine


class Etl:
    def connection(self, dsn) -> pg.Connection:
        return pg.connect(dsn)

    def create_engine(self, con) -> Engine:
        return create_engine(
            'postgresql+psycopg://',
            creator=con
        )
