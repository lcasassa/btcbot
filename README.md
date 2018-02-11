# btcbot
## Config
```
cp config.py.example config.py
```
Edit config.py with keys from: https://www.buda.com/ https://www.kraken.com/ https://labstack.com/

## Run
```
make
```
## Plot
```
make plot
open plot.png
```

## Install
### On Ubuntu
```
make install_requirements_ubuntu
make kraken_fix_ubuntu
```

### On Mac
```
make install_requirements
make kraken_fix_mac
```