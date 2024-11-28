import logging
from functools import wraps

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug(f'Calling a function {func.__name__} with arguments {args} and {kwargs}')
        return func(*args, **kwargs)
        logging.debug(f'Function {func.__name__} returned {result}')
        return result
    return wrapper