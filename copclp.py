from labstack import Client, APIError

try:
    import config
except ImportError:
    import sys
    print >> sys.stderr, 'copy config.py.example to config.py'
    sys.exit(1)

if config.labstack_accound_id == '' or config.labstack_api_key == '':
    import sys
    print >> sys.stderr, 'Please set labstack_accound_id and labstack_api_key in config.py'
    sys.exit(1)

client = Client(config.labstack_accound_id, config.labstack_api_key)


def copclp():
    try:
        response = client.currency_convert(base='COP')
    except APIError as error:
        print(error)

    cop_clp = float(response['rates']['CLP'])

    return cop_clp