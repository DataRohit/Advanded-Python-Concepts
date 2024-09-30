# Variable annotations
name: str = "Alice"
age: int = 30
is_student: bool = False


# Function annotations
def greet(person: str, age: int) -> str:
    """Greet a person by name.

    Args:
        person (str): The name of the person to greet (e.g., "Alice").
        age (int): The age of the person to greet (e.g., 30).

    Returns:
        str: The greeting message for the person (e.g., "Hello, Alice! You are 30 years old.").
    """

    return f"Hello, {person}! You are {age} years old."


# Using the function
greeting_message = greet(name, age)
print(greeting_message)

# Showing annotations
print("\nFunction annotations:", greet.__annotations__)
print("Variable annotations:", __annotations__)
