"""Base abstract class"""
import requests
from abc import ABC, abstractproperty


class JsonApi(ABC):
    @abstractproperty
    def base_url(self):
        pass

    @abstractproperty
    def version(self):
        pass

    def get(self, method_name, params={}):
        request = requests.get(self._create_url(method_name), params=params)
        return request.json()

    def _create_url(self, method_name):
        return self.base_url + "/" + self.version + "/" + method_name

    def post(self, method_name, params={}):
        url = self._create_url(method_name)
        headers = self._create_headers()
        request = requests.post(url, headers=headers, params=params)
        return request.json()

    def _create_headers(self):
        return {}
