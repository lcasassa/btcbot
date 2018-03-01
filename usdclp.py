import sys
import requests
from datetime import datetime, timedelta

try:
    import config
except ImportError:
    print >> sys.stderr, 'copy config.py.example to config.py'
    sys.exit(1)

if config.apilayer_api_key == '':
    print >> sys.stderr, 'Please set apilayer_api_key in config.py'
    sys.exit(1)

last = datetime.now() - timedelta(hours=3)
cache = 0


def usdclp():
    global cache, last
    if datetime.now() - last > timedelta(hours=1, minutes=30):
        try:
            print >> sys.stderr, 'asking for usd/clp'
            sys.stderr.flush()
            payload = {"access_key": config.apilayer_api_key, "source": "USD", "currencies": "CLP", "format": "1"}
            r = requests.get('http://apilayer.net/api/live', params=payload)
            r = r.json()

        except Exception as error:
            print(error)
            raise error

        usd_clp = float(r['quotes']['USDCLP'])
        cache = usd_clp
    else:
        usd_clp = cache

    return usd_clp
