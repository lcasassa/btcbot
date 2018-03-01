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


def copclp():
    try:
        payload={"access_key": config.apilayer_api_key, "source": "USD", "currencies": "CLP, COP", "format": "1"}
        r = requests.get('http://apilayer.net/api/live', params=payload)
        r = r.json()

    except Exception as error:
        print(error)
        raise error

    cop_clp = float(r['quotes']['USDCOP']) / float(r['quotes']['USDCLP'])

    return cop_clp