try:
    import sys
    import time
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

while True:
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
        b = {'ask': {'clp': 5273580.0, 'vol': 0.25777186}, 'bid': {'clp': 5190001.0, 'vol': 0.0871033}}
        bc = {'ask': {'cop': 5273580.0, 'vol': 0.25777186}, 'bid': {'cop': 5190001.0, 'vol': 0.0871033}}
        k = {'ask': {'usd': 8275.3, 'vol': 4.0}, 'bid': {'usd': 8258.0, 'vol': 0.6}}
        u = 604.8
        c = 123.5


    from pprint import pprint as pp

    #pp({'Saldo Buda': sb})
    #pp({'Saldo Kraken': sk})
    #pp({'Ordenes Buda': b})
    #pp({'Ordenes Kraken': k})
    #pp({'CLP/USD': u})

    p_kb = (k['ask']['usd'] - b['bid']['clp']/u) / (b['bid']['clp']/u)
    p_bk = (b['ask']['clp']/u - k['bid']['usd']) / (b['bid']['clp']/u)

    p_bbc = (bc['ask']['cop'] - b['bid']['clp']/c) / (b['bid']['clp']/c)
    p_bcb = (b['ask']['clp']/c - bc['bid']['cop']) / (b['bid']['clp']/c)

    #import math
    #pp({'usd -> btc | btc -> clp': math.floor(p_kb*100*100)/100})
    #pp({'clp -> btc | btc -> usd': math.floor(p_bk*100*100)/100})

    r = {'date': date, 'sb': sb, 'sbc': sbc, 'sk': sk, 'b': b, 'bc': bc, 'c': c, 'k': k, 'u': u, 'p_kb': p_kb, 'p_bk': p_bk, 'p_bbc': p_bbc, 'p_bcb': p_bcb, 'total': int(sb['clp'] + sbc['cop']*c)}

    r.update({'ask_bc': 0, 'bid_b': 0})
    if p_bcb > 13/100.0:
        v = min(b['bid']['vol'], bc['ask']['vol'], 0.001, sb['cop']/bc['ask']['cop'])
        p = p_bcb

        if v > 0.0005:
            print >> sys.stderr, '++++++ v =', v, 'p =', p*100.0, 'total = ', r['total'], datetime.datetime.now()
            sys.stderr.flush()

            buda_cop.oc(v, bc['ask']['cop'])
            buda.ov(v, b['bid']['clp'])

            r.update({'v': -v, 'p': p, 'ask_bc': bc['ask']['cop'], 'bid_b': b['bid']['clp']})

    r.update({'ask_b': 0, 'bid_bc': 0})
    if p_bbc > -11/100.0:
        v = min(bc['bid']['vol'], b['ask']['vol'], 0.001, sbc['clp']/b['ask']['clp'])
        p = p_bbc
        if v > 0.0005:
            print >> sys.stderr, '------ v =', v, 'p =', p*100.0, 'total = ', r['total'], datetime.datetime.now()
            sys.stderr.flush()

            buda.oc(v, b['ask']['clp'])
            buda_cop.ov(v, bc['bid']['cop'])

            r.update({'v': v, 'p': p, 'ask_b': b['ask']['clp'], 'bid_bc': bc['bid']['cop']})

    if 'v' not in r:
        r['v'] = 0
        r['p'] = 0

        #print >> sys.stderr, '       v =', r['v'], 'p =', r['p']*100.0, 'total = ', r['total']
        sys.stderr.flush()

    print(json.dumps(r))
    sys.stdout.flush()

    #if r['v'] != 0:
    #    time.sleep(60)

    time.sleep(2)
