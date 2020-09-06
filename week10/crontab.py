from apscheduler.schedulers.blocking import BlockingScheduler
import time
from functools import wraps
import os

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
def job():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    spider_dir = os.path.join(base_dir, 'mySpider')
    os.chdir(spider_dir)
    os.system('python3 start.py')

scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', hour='5', minute='0')
scheduler.start()