import pytest

from main.utils.assertions import CustomAsserts as Ca
from main.queries.query_bitcoin_values import QueryBitcoinValues as Qbv


def test_satoshi_genesis_address_received_more_than_60_btc():
    query = Qbv().get_received_by_address('genesis_address')
    Ca.value_greater_than(query, 60)


# Note per documentation, commenting below test due to following:
#   Please limit your queries to a maximum of 1 every 10 seconds.
# def test_twenty_four_hour_bitcoin_sent_not_zero():
#     query = Qbv().get_twenty_four_hour_bitcoin_sent()
#     Ca.value_is_greater_than_0(query)


if __name__ == '__main__':
    pytest.main()
