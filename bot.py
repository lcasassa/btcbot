try:
    import sys
    import json
    import buda
    import buda_cop
    import kraken
    import usdclp
    import copclp
    import datetime
except Exception as e:
    print >> sys.stderr, e
    sys.exit(1)

fetch = True
if fetch:
    date = str(datetime.datetime.now()).split(".")[0]
    try:
        sb = buda.saldo()
        sbc = buda_cop.saldo()
        sk = kraken.saldo()
        b = buda.bidask()
        bc = buda_cop.bidask()
        k = kraken.bidask()
        u = usdclp.usdclp()
        c = copclp.copclp()
    except Exception as e:
        print >> sys.stderr, e
        sys.exit(1)
else:
    date = '2018-02-10 23:20:27'
    sb = {'btc': 0.0, 'clp': 0.45}
    sbc = {'btc': 0.0, 'cop': 0.46}
    sk = {'btc': 0.03690466, 'usd': 0}
    b = {'ask': {'btc': 5273580.0, 'vol': 0.25777186}, 'bid': {'btc': 5190001.0, 'vol': 0.0871033}}
    k = {'ask': {'btc': 8275.3, 'vol': 4.0}, 'bid': {'btc': 8258.0, 'vol': 0.6}}
    u = 604.8
    c = 123.5


from pprint import pprint as pp

#pp({'Saldo Buda': sb})
#pp({'Saldo Kraken': sk})
#pp({'Ordenes Buda': b})
#pp({'Ordenes Kraken': k})
#pp({'CLP/USD': u})

p_kb = (b['bid']['btc']/u - k['ask']['btc']) / (b['bid']['btc']/u)
p_bk = (k['bid']['btc'] - b['ask']['btc']/u) / (b['bid']['btc']/u)

p_bbc = (b['bid']['btc']/c - bc['ask']['btc']) / (b['bid']['btc']/c)
p_bcb = (bc['bid']['btc'] - b['ask']['btc']/c) / (b['bid']['btc']/c)

#import math
#pp({'usd -> btc | btc -> clp': math.floor(p_kb*100*100)/100})
#pp({'clp -> btc | btc -> usd': math.floor(p_bk*100*100)/100})

r = {'date': date, 'sb': sb, 'sbc': sbc, 'sk': sk, 'b': b, 'bc': bc, 'c': c, 'k': k, 'u': u, 'p_kb': p_kb, 'p_bk': p_bk, 'p_bbc': p_bbc, 'p_bcb': p_bcb}

if p_bbc > 15/100.0: # 9.3
    v = min(b['bid']['vol'], bc['ask']['vol'], 0.001)
    p = p_bbc

    buda.oc(v, b['ask']['btc'])
    buda_cop.ov(v, bc['bid']['btc'])

    r.update({'v': -v, 'p': p, 'ask_b': b['ask']['btc'], 'bid_bc': bc['bid']['btc']})
else:
    r.update({'ask_b': 0, 'bid_bc': 0})

if p_bcb > -10/100.0: # -15.1
    v = min(bc['bid']['vol'], b['ask']['vol'], 0.001)
    p = p_bcb

    buda_cop.oc(v, bc['ask']['btc'])
    buda.ov(v, b['bid']['btc'])

    r.update({'v': v, 'p': p, 'ask_bc': bc['ask']['btc'], 'bid_b': b['bid']['btc']})
else:
    r.update({'ask_bc': 0, 'bid_b': 0})

if 'v' not in r:
    r['v'] = 0
    r['p'] = 0

print(json.dumps(r))

if r['v'] != 0:
    print >> sys.stderr, '****** v =', r['v'], 'p =', r['p']
    import time
    time.sleep(60)
else:
    print >> sys.stderr, 'v =', r['v'], 'p =', r['p']
