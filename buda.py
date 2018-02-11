from pprint import pprint as pp
import surbtc

try:
    import config
except ImportError:
    print 'copy config.py.example to config.py'
    import sys
    sys.exit(1)

if config.buda_llave == '' or config.buda_secreto == '':
    print 'Please set buda_llave and buda_secreto in config.py'
    import sys
    sys.exit(1)

client = surbtc.Client(config.buda_llave, config.buda_secreto)
market = surbtc.Market('btc-clp', client)


def bidask():
    book = market.getBook()

    # bids alguien quiere comprar
    bids = float(book['bids'][0][0])
    bids_volume = float(book['bids'][0][1])

    # bids alguien quiere vender
    asks = float(book['asks'][0][0])
    asks_volume = float(book['asks'][0][1])

    return {'bid': {'btc': bids, 'vol': bids_volume}, 'ask': {'btc': asks, 'vol': asks_volume}}


def saldo():
    clp = float(client.getBalance('clp')['available_amount'][0])
    btc = float(client.getBalance('btc')['available_amount'][0])
    return {'clp': clp, 'btc': btc}
