import sys

if sys.version_info >= (3, 0):
    from urllib.request import urlopen
else:
    from urllib2 import urlopen

import re

def usdclp():
    # get html
    response = urlopen('https://www.google.com/finance/converter?a=1&from=USD&to=CLP')
    html = response.read()

    # parse html
    m = re.search('<div id=currency_converter_result>1 USD = <span class=bld>(?P<clp>[-+]?\d*\.\d+|\d+) CLP<\/span>', str(html))
    usd_clp_str = m.group('clp')

    # str to float
    usd_clp = float(usd_clp_str)

    return usd_clp

