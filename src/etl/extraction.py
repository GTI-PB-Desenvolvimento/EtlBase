from .interfaces import Etl


class BaseExtraction(Etl):
    def __init__(self, dsn_db):
        self.engine = self.create_engine(
            self.connection(dsn_db)
        )
