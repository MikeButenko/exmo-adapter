import unittest
from unittest.mock import patch, Mock
import pytest

from algotrader.exchange.api.exceptions import InvalidPair
from algotrader.exchange.api.exmo.public_api import PublicApi
from algotrader.exchange.order_book import OrderBook


class TestPublicApi(object):

    def test_get_order_book(self):
        pass

    @patch('algotrader.exchange.api.JsonApi.get')
    def test_get_trades(self, mock_json_api_get):
        pair = "foo"
        params = {"pair": pair}
        buy_trades = [{"type": "buy", "foo": "bar"}]
        sell_trades = [{"type": "sell", "foo": "foo"}]
        trades = sell_trades + buy_trades
        mock_json_api_get.return_value = {pair: trades}
        api = PublicApi(pair)
        assert api.get_trades() == buy_trades
        mock_json_api_get.assert_called_once_with("trades", params=params)

    @patch('algotrader.exchange.api.JsonApi.get')
    def test_get_trades_raises_error(self, mock_json_api_get):
        pair = "foo"
        mock_json_api_get.return_value = {}
        api = PublicApi(pair)
        with pytest.raises(InvalidPair):
            api.get_trades()
