from time import sleep
from functools import wraps


def delay(func):
    @wraps(func)
    def wrapper(*args):
        sleep(3)
        return func(*args)

    return wrapper
