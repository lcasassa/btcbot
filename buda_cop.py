from pprint import pprint as pp
import surbtc
from requests.exceptions import ConnectionError
import sys
import math
import timeout

try:
    import config
except ImportError:
    print >> sys.stderr, 'copy config.py.example to config.py'
    sys.exit(1)

if config.buda_llave == '' or config.buda_secreto == '':
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
    btc = math.floor(float(client.getBalance('btc')['available_amount'][0]) * 1000000) / 1000000

    return {'cop': cop, 'btc': btc}


def order(client, market, type, vol, btc):
    o_id = None
    try:
        o = client.createOrder(market, type, vol, btc, 'limit')
        o_id = o['id']
        os = client.getOrder(o_id)
        timeout.set_timeout(10)
        while os['state'] == 'pending' or os['state'] == 'received':
            os = client.getOrder(o_id)
        timeout.stop_timeout()
        if os['state'] == 'canceled':
            print >> sys.stderr, "Order Canceled by user?... order_id:", o_id, "market:", market, "type:", type, "vol:", vol, "btc:", btc
            sys.stderr.flush()
            raise EnvironmentError("Orden" + str(o_id) + "cancelado por el usuario?")
    except timeout.TimeoutError as e:
        print >> sys.stderr, "Timeout... market:", market, "type:", type, "vol:", vol, "btc:", btc, str(e)
        sys.stderr.flush()
        raise e
    except ConnectionError as e:
        print >> sys.stderr, "Connection error... market:", market, "type:", type, "vol:", vol, "btc:", btc, str(e)
        sys.stderr.flush()
        raise e
    finally:
        if o_id is not None and 'os' in locals() and 'state' in os and (os['state'] not in ['traded']):
            client.cancelOrder(o_id)

    return os if 'os' in locals() else None


def oc(vol, btc):
    return order(client, 'btc-cop', 'Bid', vol, btc)


def ov(vol, btc):
    return order(client, 'btc-cop', 'Ask', vol, btc)
