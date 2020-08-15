import time
from functools import wraps

def timer(func):
    @wraps(func)
    def consume_time(*args, **kwargs):
        t1 = time.time()
        func_result = func(*args, **kwargs)
        t2 = time.time()
        print(f"@timer: {func.__name__} consume {t2 - t1: .3f} s")
        return func_result
    return consume_time

@timer
def test(*args, **kwargs):
    for i in args:
        print(i)
    time.sleep(1)
    for k in kwargs.keys():
        print(k,kwargs[k])
test(1,6,7,8,python=90,java=60)