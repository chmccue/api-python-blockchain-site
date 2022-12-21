from pprint import pprint
import config


class UnauthenticatedPages:
    """converting the following unauthenticated rest calls for blockchain.com to Python."""
    def level_2_order_book(self, symbol):
        return self._get_rest_json(f'l2/{symbol}')

    def level_3_order_book(self, symbol):
        return self._get_rest_json(f'l3/{symbol}')

    def get_tickers(self):
        return self._get_rest_json('tickers')

    def get_ticker(self, symbol):
        return self._get_rest_json(f'tickers/{symbol}')

    def get_symbols(self):
        return self._get_rest_json('symbols')

    def get_symbol(self, symbol):
        return self._get_rest_json(f'symbols/{symbol}')

    def _get_rest_json(self, url):
        return config.rest_request.get(url, headers="accept: application/json").json_dict


# sandbox testing
if __name__ == '__main__':
    pprint(UnauthenticatedPages().get_tickers())
