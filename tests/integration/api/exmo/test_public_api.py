import pytest

from algotrader.exchange.api.exceptions import InvalidPair
from algotrader.exchange.api.exmo.public_api import PublicApi


class TestPublicApi(object):
    def test_get_trades(self):
        api = PublicApi(pair="BTC_USD")
        trades = api.get_trades()
        assert type(trades) == list

    def test_get_trades_invalid_pair(self):
        api = PublicApi(pair="foo")
        with pytest.raises(InvalidPair):
            api.get_trades()

    # def test_get_order_book_asks(self):
    #     api = PublicApi(pair="BTC_USD")
    #     asks = api.get_order_book_asks()
    #     assert type(asks) == dict
    #
    # def test_get_order_book_bids(self):
    #     api = PublicApi(pair="BTC_USD")
    #     bids = api.get_order_book_bids()
    #     assert type(bids) == dict
