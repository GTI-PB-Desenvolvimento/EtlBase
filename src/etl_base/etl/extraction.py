import json
from dataclasses import dataclass

import requests as rq
from requests.auth import HTTPBasicAuth

from .interfaces import Etl


@dataclass
class ElasticInstance:
    url: str
    user: str
    password: str


class BaseExtraction(Etl):
    def __init__(self, dsn_db):
        self.engine = self.create_engine(
            self.connection(dsn_db)
        )
        self.rq = rq.session()


class BaseElasticExtraction(BaseExtraction):
    def __init__(self, dsn_db, instance: ElasticInstance, **kwargs):
        super().__init__(dsn_db)
        self.rq.headers = {'Content-Type': 'application/json'}
        self.rq.auth = HTTPBasicAuth(
            instance.user, instance.password
        )
        self._url = instance.url
        
        self._scroll = kwargs.get('scroll', '1m')
        self._size = kwargs.get('size', '1000')

        self._scroll_id = None

    @property
    def _path(self):
        if self._scroll_id:
            return '{url}/scroll'.format(url=self._url)
            
        return '{url}?scroll={scroll}&size={size}'.format(
            url=self._url, scroll=self._scroll, size=self._size
        )

    @property
    def query(self):
        return {'query': {'match_all': {}}}

    @property
    def _body(self):
        if not self._scroll_id:
            return {
                'scroll_id': self._scroll_id,
                'scroll': self._scroll
            }

        return self.query

    def data(self):
        while True:
            response = rq.get(
                self._path, data = json.dumps(self._body)
            ).json()

            try:
                self._scroll_id = response['scroll_id']
            except KeyError:
                return self.data()

            if not response['hits']['hits']:
                break

            for document in response['hits']['hits']:
                yield document
