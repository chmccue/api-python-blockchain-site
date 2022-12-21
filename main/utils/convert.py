def sats_to_btc(sats):
    return float(sats) / 100000000


def test_sats_to_btc():
    """Unit tests to validate local function"""
    assert(sats_to_btc(500110) == 0.0050011)
    assert(sats_to_btc(1150011099) == 11.50011099)
    assert(sats_to_btc(500110000) == 5.0011)
    assert(sats_to_btc(12345678) == 0.12345678)
    assert(sats_to_btc(1923694300000000) == 19236943)
