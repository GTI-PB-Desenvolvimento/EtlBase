from os import getenv

import psycopg as pg
from psycopg import Connection
from sqlalchemy import create_engine, Engine


class DsnNotInformedException(Exception):
    pass


def pg_connection(**kwargs) -> Connection:
    """
    Cria uma conexão com um banco postgresql utilizando a variável
    de ambiente PG_DSN como configuração.

    PG_DSN deve ser uma connection string no esquema Key/Value. Para
    mais informações, verificar a Documentação do postgres:
    https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-KEYWORD-VALUE

    :param dsn: connection string que substitui PG_DSN caso seja informada.
    
    Também é possivel passar configurações do próprio psycopg, para isso 
    basta verificar a documentação de conexão do mesmo:
    https://www.psycopg.org/psycopg3/docs/api/connections.html#psycopg.Connection
    """
    try:
        dsn = kwargs.pop('dsn')
    except KeyError:
        dsn = getenv('PG_DSN')
        if not dsn:
            raise DsnNotInformedException(
                'É necessário informar o DSN de conexão'
            )

    return pg.connect(conninfo=dsn, **kwargs)


def pg_engine(**kwargs) -> Engine:
    '''
    Cria um Sqlalchemy Engine utilizando uma psycopg Connection.
    Por padrão se utliza da funcão pg_connection para gerar a conexão.

    :param creator: substitui a função padrão, utilizando uma psycopg
    Connection com as configurações escolhidas pelo usuário.

    Também é possivel passar configurações da engine, para isto basta verificar
    a documentação de Engine do Sqlalchemy:
    https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine
    '''
    try:
        creator = kwargs.pop('creator')
    except KeyError:
        creator = pg_connection

    return create_engine(
        'postgresql+psycopg://',
        creator=creator,
        **kwargs
    )
