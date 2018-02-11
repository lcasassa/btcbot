from labstack import Client, APIError
import config

if config.labstack_accound_id == '' or config.labstack_api_key == '':
    print 'Please set up labstack_accound_id and labstack_api_key in config.py'

client = Client(config.labstack_accound_id, config.labstack_api_key)


def usdclp():
    try:
        response = client.currency_convert(base='USD')
    except APIError as error:
        print(error)

    usd_clp = float(response['rates']['CLP'])

    return usd_clp
