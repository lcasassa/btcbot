
import pandas as pd # Version 0.21.0
import matplotlib
from datetime import timedelta
matplotlib.use('Agg') # Force matplotlib to not use any Xwindows backend.
from matplotlib import pyplot as plt

filename = 'btcbot.log'
df = pd.read_json(filename, lines=True)[-2*24*60*60/3:]
date = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S', utc='America/Santiago')

if 1:
    my_dpi = 96
    #p = data['p'].replace('%','',regex=True).astype('float')/100
    plt.figure(figsize=(800 / my_dpi, 800 / my_dpi), dpi=my_dpi)

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    line1, = ax1.plot(date, df['p_kb']*100, '.', label='p_kb')
    line2, = ax1.plot(date, df['p_bk']*100, '.', label='p_bk')
    line3, = ax1.plot(date, df['p_bbc']*100, '*', label='p_bbc')
    line4, = ax1.plot(date, df['p_bcb']*100, '*', label='p_bcb')
    line5, = ax2.plot(date, df['total'], '*', label='total clp')
    ax1.legend([line1, line2, line3, line4])
    ax2.legend([line5])

    fig.autofmt_xdate()
    import matplotlib.dates as mdates
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d %H:%M'))

    plt.savefig('plot.png', dpi=my_dpi*2)
