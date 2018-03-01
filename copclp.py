import requests
from datetime import datetime, timedelta

try:
    import config
except ImportError:
    import sys
    print >> sys.stderr, 'copy config.py.example to config.py'
    sys.exit(1)

if config.apilayer_api_key == '':
    import sys
    print >> sys.stderr, 'Please set apilayer_api_key in config.py'
    sys.exit(1)

last = datetime.now() - timedelta(hours=3)
cache = 0


def copclp():
    global cache, last
    if datetime.now() - last > timedelta(hours=1, minutes=30):
        try:
            print >> sys.stderr, 'asking for cop/clp'
            sys.stderr.flush()
            payload = {"access_key": config.apilayer_api_key, "source": "USD", "currencies": "CLP, COP", "format": "1"}
            r = requests.get('http://apilayer.net/api/live', params=payload)
            r = r.json()

        except Exception as error:
            print(error)
            raise error

        cop_clp = float(r['quotes']['USDCLP']) / float(r['quotes']['USDCOP'])
        cache = cop_clp
    else:
        cop_clp = cache

    return cop_clp
