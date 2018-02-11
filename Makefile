run:
	while true; do python bot.py | tee -a btcbot.log; sleep 10; done;

plot:
	python plotall.py
