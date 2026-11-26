class NumberSequence:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return (number for number in range(self.start, self.stop))


if __name__ == "__main__":
    numbers = NumberSequence(1, 68)
    generator = iter(numbers)

    print(f"Generator: {generator}")
    print("Values:", list(generator))