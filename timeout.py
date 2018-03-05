import signal


class TimeoutError(Exception):
    pass


def _sig_alarm(sig, tb):
    raise TimeoutError("timeout")


signal.signal(signal.SIGALRM, _sig_alarm)


def set_timeout(timeout):
    signal.alarm(timeout)


def stop_timeout(timeout):
    signal.alarm(0)
