run:
	while true; do python bot.py 2> error.log | tee -a btcbot.log; sleep 10; done;

plot:
	python plotall.py

install_requirements:
	pip install --user -r requirements.txt

install_requirements_ubuntu:
	sudo apt-get install -y git make python-pip python-matplotlib
	pip install --user --no-cache-dir -r requirements.txt

kraken_fix_ubuntu:
	cp api.py.diff ~/.local/lib/python2.7/site-packages/krakenex/
	cp ~/.local/lib/python2.7/site-packages/krakenex/api.py ~/.local/lib/python2.7/site-packages/krakenex/api.py_ori
	cd ~/.local/lib/python2.7/site-packages/krakenex/ && git apply api.py.diff
	rm ~/.local/lib/python2.7/site-packages/krakenex/api.py.diff

kraken_fix_mac:
	cp api.py.diff ~/Library/Python/2.7/lib/python/site-packages/krakenex/
	cp ~/Library/Python/2.7/lib/python/site-packages/krakenex/api.py ~/Library/Python/2.7/lib/python/site-packages/krakenex/api.py_ori
	cd ~/Library/Python/2.7/lib/python/site-packages/krakenex/ && git apply api.py.diff
	rm ~/Library/Python/2.7/lib/python/site-packages/krakenex/api.py.diff
