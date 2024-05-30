import time
import gevent

def foo():
    start_time = time.time()
    print('开始 foo')
    gevent.sleep(1)
    print(f'\t上下文回到 foo again, 耗时: {time.time() - start_time:.2f}秒')


def bar():
    start_time = time.time()
    print('上下文切换到 bar')
    gevent.sleep(1)
    print(f'\t上下文回到 bar, 耗时: {time.time() - start_time:.2f}秒')


def main():
    start_time = time.time()
    gevent.joinall([
        gevent.spawn(foo),
        gevent.spawn(bar),
    ])
    print(f"总共耗时: {time.time() - start_time:.2f}秒")


if __name__ == '__main__':
    main()

