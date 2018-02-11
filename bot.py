import buda
import kraken
import usdclp
import datetime

fetch = True
if fetch:
    date = str(datetime.datetime.now()).split(".")[0]
    sb = buda.saldo()
    sk = kraken.saldo()
    b = buda.bidask()
    k = kraken.bidask()
    u = usdclp.usdclp()
else:
    date = '2018-02-10 23:20:27'
    sb = {'btc': 0.0, 'clp': 0.45}
    sk = {'btc': 0.03690466, 'usd': 0}
    b = {'ask': {'btc': 5273580.0, 'vol': 0.25777186}, 'bid': {'btc': 5190001.0, 'vol': 0.0871033}}
    k = {'ask': {'btc': 8275.3, 'vol': 4.0}, 'bid': {'btc': 8258.0, 'vol': 0.6}}
    u = 604.8


from pprint import pprint as pp

#pp({'Saldo Buda': sb})
#pp({'Saldo Kraken': sk})
#pp({'Ordenes Buda': b})
#pp({'Ordenes Kraken': k})
#pp({'CLP/USD': u})

p_kb = (b['bid']['btc']/u - k['ask']['btc']) / (b['bid']['btc']/u)
p_bk = (k['bid']['btc'] - b['ask']['btc']/u) / (b['bid']['btc']/u)

#import math
#pp({'usd -> btc | btc -> clp': math.floor(p_kb*100*100)/100})
#pp({'clp -> btc | btc -> usd': math.floor(p_bk*100*100)/100})

import json
print(json.dumps({'date': date, 'sb': sb, 'sk': sk, 'b': b, 'k':k, 'u': u, 'p_kb': p_kb, 'p_bk': p_bk}))
