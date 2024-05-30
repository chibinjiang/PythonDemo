import time
import gevent
from gevent import Timeout

seconds = 10

timeout = Timeout(seconds)
timeout.start()

def wait():
    start_time = time.time()
    print('Start wating....')
    gevent.sleep(seconds)
    print(f'End waiting after {time.time() - start_time:.2f} Seconds')


def main():
    try:
        gevent.spawn(wait).join()
    except Timeout:
        print('Could not complete')


if __name__ == '__main__':
    main()

