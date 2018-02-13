from algotrader.utils.json_api import JsonApi


class BaseApi(JsonApi):
    BASE_URL = "https://api.exmo.com"
    VERSION = "v1"
    HEADERS = {}

    @property
    def base_url(self):
        return BaseApi.BASE_URL

    @property
    def version(self):
        return BaseApi.VERSION

    def _create_headers(self):
        return BaseApi.HEADERS
