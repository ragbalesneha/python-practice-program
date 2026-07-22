class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            val = self.current
            self.current += 1
            return val
        raise StopIteration

# Usage
for num in Counter(3):
    print(num)  # Prints 1, 2, 3