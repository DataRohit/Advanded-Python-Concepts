def my_decorator(func):
    """
    A simple decorator that prints a message before and after the execution of the function.
    """

    def wrapper(*args: tuple[any], **kwargs: dict[str, any]) -> any:
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result

    return wrapper


@my_decorator
def say_hello(name: str):
    """
    A simple function that greets the user.
    """
    print(f"Hello, {name}!")


@my_decorator
def add(a: int | float, b: int | float) -> int | float:
    """
    A simple function that adds two numbers.
    """
    return a + b


if __name__ == "__main__":
    # Using the decorator with the say_hello function
    say_hello("Alice")

    # Add a line break
    print()

    # Using the decorator with the add function
    result = add(3, 5)
    print(f"The result of the addition is: {result}")
