from algotrader.exchange.api import BaseApi
from algotrader.exchange.api.exceptions import InvalidPair
from algotrader.exchange.order_book import OrderBook


class PublicApi(BaseApi):
    def __init__(self, pair):
        self.pair = pair

    def get_trades(self):
        method_name = "trades"
        data = self.get(method_name, params={"pair": self.pair})
        trades = [trade for trade in data if trade["type"] == "buy"]
        return trades

    def get(self, method_name, params={}):
        data = super().get(method_name, params)
        self.__validate_response_data(data)
        return data[self.pair]

    def __validate_response_data(self, data):
        if self.pair not in data:
            raise InvalidPair("Invalid pair: " + self.pair)

    def get_order_book(self):
        method_name = "order_book"
        data = self.get(method_name, params={"pair": self.pair})
        self.__prepare_orders(data["ask"], data["bid"])
        order_book = OrderBook()

        order_book.asks = data["ask"]
        order_book.ask_amount = float(data["ask_amount"])
        order_book.ask_quantity = float(data["ask_quantity"])

        order_book.bids = data["bid"]
        order_book.bid_amount = float(data["bid_amount"])
        order_book.bid_quantity = float(data["bid_quantity"])

        return order_book

    @staticmethod
    def __prepare_orders(*args):
        for orders in args:
            for data in orders:
                data[0] = float(data[0])
                data[1] = float(data[1])
                del data[2]
