from labstack import Client, APIError

try:
    import config
except ImportError:
    print 'copy config.py.example to config.py'
    import sys
    sys.exit(1)

if config.labstack_accound_id == '' or config.labstack_api_key == '':
    print 'Please set labstack_accound_id and labstack_api_key in config.py'
    import sys
    sys.exit(1)

client = Client(config.labstack_accound_id, config.labstack_api_key)


def usdclp():
    try:
        response = client.currency_convert(base='USD')
    except APIError as error:
        print(error)

    usd_clp = float(response['rates']['CLP'])

    return usd_clp
