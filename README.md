# btcbot
```
make install_requirements
make
make plot
open plot.png
```

### On Mac
If you see:
```
  File "/Users/lcasassa/Library/Python/2.7/lib/python/site-packages/krakenex/api.py", line 26, in <module>
    import urllib.parse
ImportError: No module named parse
```
do:
```

make kraken_mac_fix
```