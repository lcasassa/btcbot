run:
	while true; do python bot.py | tee -a btcbot.log; sleep 10; done;

plot:
	python plotall.py

install_requirements:
	pip install --user -r requirements.txt

kraken_mac_fix:
	cp api.py.diff ~/Library/Python/2.7/lib/python/site-packages/krakenex/
	cp ~/Library/Python/2.7/lib/python/site-packages/krakenex/api.py ~/Library/Python/2.7/lib/python/site-packages/krakenex/api.py_ori
	cd ~/Library/Python/2.7/lib/python/site-packages/krakenex/ && git apply api.py.diff
	rm ~/Library/Python/2.7/lib/python/site-packages/krakenex/api.py.diff
