from main.utils import convert
from config import query_request

path_urls = dict(
    totalbc='totalbc',
    twentyfourhrbtcsent='24hrbtcsent',
    receivedbyaddress='getreceivedbyaddress/',
    sentbyaddress='getsentbyaddress/',
    addressbalance='addressbalance/',
    txtotalbtcoutput='txtotalbtcoutput/',
    txtotalbtcinput='txtotalbtcinput/',
    txfee='txfee/'
)

bc_addresses = dict(
    genesis_address='1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
    mt_gox_hacker_address='1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF'
)


def get_by_address(url, address):
    return convert.sats_to_btc(
        query_request.get(path_urls.get(url) + bc_addresses.get(address)).text)


class QueryBitcoinValues:
    def get_total_circulating_bitcoin(self):
        return self.get_btc_value('totalbc')

    def get_twenty_four_hour_bitcoin_sent(self):
        return self.get_btc_value('twentyfourhrbtcsent')

    def get_tx_fee(self, address):
        return get_by_address('txfee', address)

    def get_tx_total_input(self, address):
        return get_by_address('txtotalbtcinput', address)

    def get_tx_total_output(self, address):
        return get_by_address('txtotalbtcoutput', address)

    def get_address_balance(self, address):
        return get_by_address('addressbalance', address)

    def get_sent_by_address(self, address):
        return get_by_address('sentbyaddress', address)

    def get_received_by_address(self, address):
        return get_by_address('receivedbyaddress', address)

    def get_btc_value(self, url):
        return convert.sats_to_btc(query_request.get(path_urls.get(url)).text)


# sandbox testing
if __name__ == '__main__':
    print(QueryBitcoinValues().get_received_by_address('genesis_address'))
