def count_up_to(max_value: int):
    current = 1
    while current <= max_value:
        yield current
        current += 1


if __name__ == "__main__":
    counter = count_up_to(100_000)

    for number in counter:
        print(number)
