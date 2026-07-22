import time

def timer_decorator(func):
    """Measures the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[{func.__name__}] took {end_time - start_time:.4f} seconds to run.")
        return result
    return wrapper

# Applying the decorator
@timer_decorator
def process_data(items):
    total = 0
    for item in items:
        total += item ** 2
    return total

# Usage
data = list(range(1_000_000))
print(f"Result: {process_data(data)}")