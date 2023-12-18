from os import getenv

import psycopg as pg
from sqlalchemy import create_engine, Engine


class Etl:
    def __init__(self):
        self.engine = self.__engine()

    def __connection(self) -> pg.Connection:
        return pg.connect(
            dbname=getenv('PG_NAME'),
            user=getenv('PG_USER'),
            password=getenv('PG_PWD'),
            host=getenv('PG_HOST'),
            port=getenv('PG_PORT')
        )

    def __engine(self) -> Engine:
        return create_engine(
            'postgresql+psycopg://',
            creator=self.__connection
        ) 

