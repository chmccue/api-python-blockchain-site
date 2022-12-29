import pytest
from main.utils.schema_validators import SchemaValidators as Sv
from main.exchangerestapi.unauthenticated import UnauthenticatedPages as Up
from main.exchangerestapi.schema_data import schemas


@pytest.mark.blockchain
@pytest.mark.schema
class TestSchema:
    @pytest.mark.schema_single
    def test_one_symbol_has_expected_schema(self, log):
        """
        Test one symbol of Blockchain API returns expected schema pattern.
        """
        # Logging example in report
        schema_data = Up().get_symbol('BTC-USD')
        log.info(f"schema data base symbol being used: {schema_data['base_currency']}")
        Sv.one_dataset_has_expected_schema(schemas.get('symbol_schema'), schema_data)

    @pytest.mark.schema_multi
    def test_all_symbols_have_expected_schema(self):
        """
        Test all symbols of Blockchain API returns expected schema pattern.
        """
        Sv.all_datasets_have_expected_schema(schemas.get('symbol_schema'), Up().get_symbols())

    @pytest.mark.schema_single
    def test_one_ticker_has_expected_schema(self):
        """
        Test one ticker of Blockchain API returns expected schema pattern.
        """
        Sv.one_dataset_has_expected_schema(schemas.get('ticker_schema'), Up().get_ticker('BTC-USD'))

    @pytest.mark.schema_multi
    def test_all_tickers_have_expected_schema(self):
        """
        Test all tickers of Blockchain API returns expected schema pattern.
        """
        Sv.all_datasets_have_expected_schema(schemas.get('ticker_schema'), Up().get_tickers(), False)
