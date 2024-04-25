from dataclasses import dataclass

import psycopg as pg
from psycopg import Connection
from sqlalchemy import create_engine, Engine


@dataclass
class PGConfig:
    user: str
    passwd: str
    host: str
    dbname: str
    port: int = 5432


def pg_connection(config: PGConfig) -> Connection: 
    return pg.connect(
        host=config.host,
        port=config.port,
        dbname=config.dbname,
        user=config.user,
        password=config.passwd
    )


def pg_engine(config: PGConfig) -> Engine:
    return create_engine(
        'postgresql+psycopg://',
        creator=pg_connection(config)
    )
