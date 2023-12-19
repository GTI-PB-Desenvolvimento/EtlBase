from .interfaces import Etl


class BaseProcesing(Etl):
    def __init__(self, dsn_db_extraction, dsn_db_result=None):
        self.engine_db_extraction = self.create_engine(
            self.connection(dsn_db_extraction)
        )
        if dsn_db_result:
            self.engine_db_result = self.create_engine(
                self.connection(dsn_db_result)
            )
