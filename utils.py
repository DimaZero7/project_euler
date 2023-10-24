import time
import functools

import memory_profiler


def performance_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        mem_before = memory_profiler.memory_usage()[0]
        result = func(*args, **kwargs)
        end_time = time.time()
        mem_after = memory_profiler.memory_usage()[0]

        execution_time = end_time - start_time
        mem_usage = mem_after - mem_before

        print('_____________________________')
        print(f"Execution time: {execution_time:.3f} seconds")
        print(f"Used {mem_usage:.3f} MiB memories")
        return result
    return wrapper
