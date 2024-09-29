# Basic Unpacking
a, b, c = [1, 2, 3]
print(f"a: {a}, b: {b}, c: {c}\n")

# Extended Iterable Unpacking with *
a, b, *c = [1, 2, 3, 4, 5]
print(f"a: {a}, b: {b}, c: {c}\n")

# Ignoring values
a, _, c = [1, 2, 3]
print(f"a: {a}, c: {c}\n")

# Unpacking Nested Structures
data = ("John", "Doe", (25, "Python Developer"))
first_name, last_name, (age, position) = data
print(
    f"First Name: {first_name}, Last Name: {last_name}, Age: {age}, Position: {position}\n"
)


# Unpacking in Function Arguments
def print_names(*names):
    for name in names:
        print(name)
    print()


print_names("Peter Parker", "Mary Jane", "Harry Osborn")

# Combining lists with Unpacking
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]
print(f"Combined: {combined}\n")

# Unpacking Dictionaries with **
dict1 = {"name": "John", "age": 25}
dict2 = {"position": "Python Developer"}
combined = {**dict1, **dict2}
print(f"Combined: {combined}\n")

# Swapping Variables Using Unpacking
x, y = 10, 20
print(f"Before Variable - x: {x}, y: {y}")
x, y = y, x
print(f"After Variable - x: {x}, y: {y}\n")
