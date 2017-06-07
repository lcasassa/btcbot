import pandas as pd
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
from matplotlib import pyplot as plt

data = pd.read_csv('btcbot.log', sep=" ", header=None, names=['date', 'time', 'clp', '-', 'usd', '*', 'usdclp', '=', 'clpdiff', '->', 'p'])
date = pd.to_datetime(data['date'] + ' ' + data['time'], format='%Y-%m-%d %H:%M:%S')
p = data['p'].replace('%','',regex=True).astype('float')/100

fig, ax = plt.subplots(1)
ax.plot(date, p)

fig.autofmt_xdate()
import matplotlib.dates as mdates
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d %H:%M'))

plt.savefig('plot.png')
