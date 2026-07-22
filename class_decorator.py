class CallCounter:
    """Class-based decorator that tracks how many times a function is invoked."""
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Function '{self.func.__name__}' has been called {self.count} time(s).")
        return self.func(*args, **kwargs)

# Applying the class decorator
@CallCounter
def compute_square(n):
    return n * n

# Usage
print(compute_square(4))
print(compute_square(5))
print(compute_square(12))