import json
from dataclasses import dataclass

from requests.auth import HTTPBasicAuth

from .interfaces import RequestsBaseExtraction
from ..exc import SourceIdNotFoundException


@dataclass
class ElasticInstance:
    url: str
    user: str
    password: str


class BaseElasticExtraction(RequestsBaseExtraction):
    def __init__(self, instance: ElasticInstance, **kwargs):
        super().__init__()
        self.rq.headers = {'Content-Type': 'application/json'}
        self.rq.auth = HTTPBasicAuth(
            instance.user, instance.password
        )
        self._url = '/'.join([instance.url, '_search'])
        
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
        if self._scroll_id:
            return {
                'scroll_id': self._scroll_id,
                'scroll': self._scroll
            }

        return self.query

    def data(self):
        while True:
            response = self.rq.get(
                self._path, data = json.dumps(self._body)
            ).json()

            try:
                self._scroll_id = response['_scroll_id']
            except KeyError as e:
                raise SourceIdNotFoundException from e

            if not response['hits']['hits']:
                break

            for document in response['hits']['hits']:
                yield document['_source']
