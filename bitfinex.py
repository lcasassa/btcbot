import bitfinex
from pprint import pprint as pp

client = bitfinex.Client()

print client.ticker('btcusd')
ob = client.order_book('btcusd')

pp(ob)

ask = ob['asks'][0]
volumen = ask['amount']
pp(volumen)

