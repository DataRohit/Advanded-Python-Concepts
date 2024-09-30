class MyRange:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current


if __name__ == "__main__":
    # Example 1: Using the iter() function on the range object
    r = range(2, 4)
    itr = iter(r)

    # Print the elements of the range object using next()
    try:
        while True:
            print(next(itr))
    except StopIteration:
        print("Stop Iteration\n")

    # Example 2: Using the custom range object
    r = MyRange(2, 4)
    for num in r:
        print(num)
