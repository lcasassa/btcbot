#!/usr/bin/python
import httplib
import urllib
import json

''' kraken '''
headers = { 'User-Agent': 'krakenex/0.0.5 (+https://github.com/veox/python2-krakenex)'}
uri = 'api.kraken.com'
conn = httplib.HTTPSConnection(uri, timeout=30)
url = 'https://api.kraken.com/0/public/Ticker'
req =  {'pair': 'XXBTZUSD'}
data = urllib.urlencode(req)
conn.request("POST", url, data, headers)
response = conn.getresponse()

kraken = json.loads(response.read())


''' surbtc '''
uri = 'www.surbtc.com'
conn = httplib.HTTPSConnection(uri, timeout=30)
url = 'https://www.surbtc.com/api/v2/markets/btc-clp/ticker'
conn.request("GET", url)
response = conn.getresponse()

surbtc = json.loads(response.read())


''' Calculos '''
usd = kraken['result']['XXBTZUSD']['c'][0]
clp = surbtc['ticker']['last_price'][0]

usd = float(usd)
clp = float(clp)

clp_diff = clp - usd*670
clp_diff = int(clp_diff)

''' prints '''
#import pprint
#pprint.pprint(kraken)
#pprint.pprint(surbtc)

def intWithCommas(x):
    if type(x) not in [type(0), type(0L)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ".%03d%s" % (r, result)
    return "%d%s" % (x, result)

print 'clp - usd * 670',
print '=',
print intWithCommas(int(clp)), '-', ('%.2f' % (usd)).replace('.', ','), '* 670',
print '= $' + intWithCommas(clp_diff),


print '->', '%%%.2f' % (100*clp_diff / (usd * 670))
