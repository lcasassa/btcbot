from pprint import pprint as pp
import surbtc
from requests.exceptions import ConnectionError

try:
    import config
except ImportError:
    import sys
    print >> sys.stderr, 'copy config.py.example to config.py'
    sys.exit(1)

if config.buda_llave == '' or config.buda_secreto == '':
    import sys
    print >> sys.stderr, 'Please set buda_llave and buda_secreto in config.py'
    sys.exit(1)

client = surbtc.Client(config.buda_llave, config.buda_secreto)
market = surbtc.Market('btc-cop', client)


def bidask():
    book = market.getBook()

    # bids alguien quiere comprar
    bids = float(book['bids'][0][0])
    bids_volume = float(book['bids'][0][1])

    # bids alguien quiere vender
    asks = float(book['asks'][0][0])
    asks_volume = float(book['asks'][0][1])

    return {'bid': {'cop': bids, 'vol': bids_volume}, 'ask': {'cop': asks, 'vol': asks_volume}}


def saldo():
    cop = float(client.getBalance('cop')['available_amount'][0])
    btc = float(client.getBalance('btc')['available_amount'][0])
    return {'cop': cop, 'btc': btc}


def oc(vol, btc):
    while True:
        try:
            o = client.createOrder('btc-cop', 'Bid', vol, btc, 'limit')
            break
        except ConnectionError as e:
            print >> sys.stderr, "retry buda_cop.oc", str(e)
            sys.stderr.flush()
            continue
    o_id = o['id']
    os = client.getOrder(o_id)
    while os['state'] != 'traded':
        os = client.getOrder(o_id)
    return os


def ov(vol, btc):
    while True:
        try:
            o = client.createOrder('btc-cop', 'Ask', vol, btc, 'limit')
            break
        except ConnectionError as e:
            print >> sys.stderr, "retry buda_cop.ov", str(e)
            sys.stderr.flush()
            continue
    o_id = o['id']
    os = client.getOrder(o_id)
    while os['state'] != 'traded':
        os = client.getOrder(o_id)
    return os
