import pytest
from main.utils.assertions import CustomAsserts as Ca
from main.queries.query_bitcoin_values import QueryBitcoinValues as Qbv


@pytest.mark.skip(reason='per site documentation: limit queries to max of 1 per 10 seconds')
@pytest.mark.blockchain
@pytest.mark.query
class TestQueries:

    def test_satoshi_genesis_address_received_more_than_60_btc(self):
        """
        Test Satoshi's genesis address has received more than 60 BTC.
        """
        query = Qbv().get_received_by_address('genesis_address')
        Ca.value_greater_than(query, 60)

    def test_24_hour_btc_sent_not_zero(self):
        """
        Test the 24 hour sent BTC volume is greater than 0.
        """
        query = Qbv().get_twenty_four_hour_bitcoin_sent()
        Ca.value_is_greater_than_0(query)
