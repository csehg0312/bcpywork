from functools import wraps
from time import perf_counter, sleep

def get_time(func):
    """Egy fuggveny fut'si idejet meri"""
    
    @wraps(func)
    def wrapper(arg):
        start_time = perf_counter()
        
        func(arg)
        
        end_time = perf_counter()
        total_time = round(end_time - start_time, 2)
        
        print('Time is ', total_time, ' seconds')
    return wrapper