import unittest.mock
import pytest
import requests
from algotrader.utils.json_api import JsonApi


class JsonApiStub(JsonApi):
    BASE_URL = "http://foo"
    VERSION = "bar"
    HEADERS = None

    @property
    def base_url(self):
        return JsonApiStub.BASE_URL

    @property
    def version(self):
        return JsonApiStub.VERSION

    def _create_headers(self):
        return JsonApiStub.HEADERS


class TestJsonApi(object):
    @pytest.fixture
    def request_mock_builder(self, mocker):
        def builder(method, json):
            mock = mocker.patch.object(requests, method, autospec=True)
            mock.return_value.json = unittest.mock.MagicMock(return_value=json)
            return mock
        return builder

    def test_get(self, request_mock_builder):
        api = JsonApiStub()
        method_name = "foobar"
        params = {"foo": "bar"}
        expected = {"bar": "foo"}
        mock_requests_get = request_mock_builder("get", expected)
        assert api.get(method_name, params) == expected

        url = self._build_url(method_name)
        mock_requests_get.assert_called_once_with(url, params=params)

    def _build_url(self, method_name):
        return JsonApiStub.BASE_URL + "/" + JsonApiStub.VERSION + "/" + method_name

    def test_post(self, request_mock_builder):
        api = JsonApiStub()
        method_name = "foobar"
        params = {"foo": "bar"}
        expected = {"bar": "foo"}
        headers = JsonApiStub.HEADERS
        mock_requests_post = request_mock_builder("post", expected)
        assert api.post(method_name, params) == expected

        url = self._build_url(method_name)
        mock_requests_post.assert_called_once_with(url, headers=headers, params=params)
