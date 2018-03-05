from pprint import pprint as pp
import surbtc
from requests.exceptions import ConnectionError
import sys
import timeout

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
market = surbtc.Market('btc-clp', client)


def bidask():
    book = market.getBook()

    # bids alguien quiere comprar
    bids = float(book['bids'][0][0])
    bids_volume = float(book['bids'][0][1])

    # bids alguien quiere vender
    asks = float(book['asks'][0][0])
    asks_volume = float(book['asks'][0][1])

    return {'bid': {'clp': bids, 'vol': bids_volume}, 'ask': {'clp': asks, 'vol': asks_volume}}


def saldo():
    clp = float(client.getBalance('clp')['available_amount'][0])
    btc = float(client.getBalance('btc')['available_amount'][0])
    return {'clp': clp, 'btc': btc}


def order(client, market, type, vol, btc):
    o_id = None
    try:
        o = client.createOrder(market, type, vol, btc, 'limit')
        o_id = o['id']
        os = client.getOrder(o_id)
        timeout.set_timeout(10)
        while os['state'] == 'pending':
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
        if o_id is not None:
            client.cancelOrder(o_id)

    return os


def oc(vol, btc):
    return order(client, 'btc-clp', 'Bid', vol, btc)


def ov(vol, btc):
    return order(client, 'btc-clp', 'Ask', vol, btc,)
