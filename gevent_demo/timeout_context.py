import time
import gevent
from gevent import Timeout


time_to_wait = 5  # seconds


class TooLong(Exception):
    pass


def task_to_wait():
    start_time = time.time()
    print('Starting waiting .....')
    gevent.sleep(10)
    print(f'Task Finished After {time.time() - start_time:.2f} Seconds')


def main():
    with Timeout(time_to_wait, TooLong):
         task_to_wait()


if __name__ == '__main__':
    main()


