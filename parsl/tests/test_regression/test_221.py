import pytest

import parsl
from parsl.app.app import App
from parsl.tests.configs.local_ipp import config

parsl.clear()
dfk = parsl.load(config)


@App('python')
def slow_double(x, dur=0.1):
    import time
    time.sleep(dur)
    return x * 5


@pytest.mark.local
def test_cleanup_behavior_221():
    """ A1 A2 A3   -> cleanup
        B1 B2 B3

    """

    round_1 = []
    for i in range(0, 2):
        f = slow_double(i)
        round_1.append(f)

    round_2 = []
    for i in round_1:
        f = slow_double(i)
        round_2.append(f)

    dfk.cleanup()


if __name__ == "__main__":

    test_cleanup_behavior_221()
