class OrderBook(object):

    @property
    def ask_quantity(self):
        return self.__ask_quantity

    @ask_quantity.setter
    def ask_quantity(self, value):
        self.__ask_quantity = float(value)

    @property
    def ask_amount(self):
        return self.__ask_amount

    @ask_amount.setter
    def ask_amount(self, value):
        self.__ask_amount = float(value)

    @property
    def asks(self):
        return self.__asks

    @asks.setter
    def asks(self, value):
        self.__asks = value

    @property
    def bids(self):
        return self.__bids

    @bids.setter
    def bids(self, value):
        self.__bids = value
