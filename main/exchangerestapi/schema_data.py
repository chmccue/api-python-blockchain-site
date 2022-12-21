schemas = dict(
    symbol_schema={
        'auction_price': {'type': 'number'},
        'auction_size': {'type': 'number'},
        'auction_time': {'type': 'string'},
        'base_currency': {'type': 'string'},
        'base_currency_scale': {'type': 'number'},
        'counter_currency': {'type': 'string'},
        'counter_currency_scale': {'type': 'number'},
        'id': {'type': 'number'},
        'imbalance': {'type': 'number'},
        'lot_size': {'type': 'number'},
        'lot_size_scale': {'type': 'number'},
        'max_order_size': {'type': 'number'},
        'max_order_size_scale': {'type': 'number'},
        'min_order_size': {'type': 'number'},
        'min_order_size_scale': {'type': 'number'},
        'min_price_increment': {'type': 'number'},
        'min_price_increment_scale': {'type': 'number'},
        'status': {'type': 'string'}
    },
    ticker_schema={
        'last_trade_price': {'type': 'number'},
        'price_24h': {'type': 'number'},
        'symbol': {'type': 'string'},
        'volume_24h': {'type': 'number'},
    }
)
