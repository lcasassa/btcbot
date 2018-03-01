import requests

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


def usdclp():
    try:
        payload={"access_key": config.apilayer_api_key, "source": "USD", "currencies": "CLP, COP", "format": "1"}
        r = requests.get('http://apilayer.net/api/live', params=payload)

    except Exception as error:
        print(error)
        raise error

    usd_clp = float(r.json()['quotes']['USDCLP'])

    return usd_clp