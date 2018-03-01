
import pandas as pd # Version 0.21.0
import matplotlib
matplotlib.use('Agg') # Force matplotlib to not use any Xwindows backend.
from matplotlib import pyplot as plt

filename = 'btcbot.log'
df = pd.read_json(filename, lines=True)
date = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')

if 1:

    #p = data['p'].replace('%','',regex=True).astype('float')/100

    fig, ax = plt.subplots(1)
    line1, = ax.plot(date, df['p_kb']*100, '.', label='p_kb')
    line2, = ax.plot(date, df['p_bk']*100, '.', label='p_bk')
    line3, = ax.plot(date, df['p_bbc']*100, '*', label='p_bbc')
    line4, = ax.plot(date, df['p_bcb']*100, '*', label='p_bcb')
    plt.legend(handles=[line1, line2, line3, line4])

    fig.autofmt_xdate()
    import matplotlib.dates as mdates
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d %H:%M'))

    plt.savefig('plot.png')
