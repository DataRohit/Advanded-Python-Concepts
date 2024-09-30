import itertools

# Infinite iterator
counter = itertools.count(start=10, step=2)
print(next(counter), end=" ")  # Output: 10
print(next(counter))  # Output: 12

# Cycle iterator
cycler = itertools.cycle(["A", "B", "C"])
print(next(cycler), end=" ")  # Output: A
print(next(cycler), end=" ")  # Output: B
print(next(cycler), end=" ")  # Output: C
print(next(cycler))  # Output: A (repeats)


# Combination iterator
combination = itertools.combinations(["A", "B", "C"], 2)
print(list(combination))  # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]


# Permutation iterator
permutation = itertools.permutations(["A", "B", "C"], 2)
print(
    list(permutation)
)  # Output: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
