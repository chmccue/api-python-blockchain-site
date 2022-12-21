import pytest
from main.utils.schema_validators import SchemaValidators as Sv
from main.exchangerestapi.unauthenticated import UnauthenticatedPages as Up
from main.exchangerestapi.schema_data import schemas


def test_one_symbol_has_expected_schema():
    Sv.one_dataset_has_expected_schema(schemas.get('symbol_schema'), Up().get_symbol('BTC-USD'))


def test_all_symbols_have_expected_schema():
    Sv.all_datasets_have_expected_schema(schemas.get('symbol_schema'), Up().get_symbols())


def test_one_ticker_has_expected_schema():
    Sv.one_dataset_has_expected_schema(schemas.get('ticker_schema'), Up().get_ticker('BTC-USD'))


def test_all_tickers_have_expected_schema():
    Sv.all_datasets_have_expected_schema(schemas.get('ticker_schema'), Up().get_tickers(), False)


if __name__ == '__main__':
    pytest.main()
