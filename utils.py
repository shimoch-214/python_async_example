import threading as th
from timeit import default_timer as timer


def check_th(func):
    def wrapper(*args, **kwargs):
        print(th.get_ident())
        func(*args, **kwargs)
    return wrapper

def async_timeit(func):
    async def wrapper(*args, **kwargs):
        s = timer()
        print(f'start: {func.__name__}')
        await func(*args, **kwargs)
        e = timer()
        print(f'end: {func.__name__}')
        print(e - s)
    return wrapper
