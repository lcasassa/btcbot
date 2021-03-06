from pprint import pprint as pp
import krakenex

try:
    import config
except ImportError:
    import sys
    print >> sys.stderr, 'copy config.py.example to config.py'
    sys.exit(1)

if config.kraken_api_key == '' or config.kraken_private_key == '':
    import sys
    print >> sys.stderr, 'Please set kraken_api_key and kraken_private_key in config.py'
    sys.exit(1)

api = krakenex.API(config.kraken_api_key, config.kraken_private_key)


def bidask():
    #pp(api.query_public('AssetPairs'))
    book = api.query_public('Depth', {'pair': 'XXBTZUSD'})
    bid = float(book['result']['XXBTZUSD']['bids'][0][0])
    bid_volume = float(book['result']['XXBTZUSD']['bids'][0][1])
    ask = float(book['result']['XXBTZUSD']['asks'][0][0])
    ask_volume = float(book['result']['XXBTZUSD']['asks'][0][1])
    return {'bid': {'usd': bid, 'vol': bid_volume}, 'ask': {'usd': ask, 'vol': ask_volume}}


def saldo():
    balance = api.query_private('Balance')
    if len(balance['error']) > 0:
        pp(balance['error'])
        raise ValueError(balance['error'])

    btc = 0
    if 'XXBT' in balance['result']:
        btc = float(balance['result']['XXBT'])

    usd = 0
    if 'ZUSD' in balance['result']:
        usd = float(balance['result']['ZUSD'])

    return {'usd': usd, 'btc': btc}
