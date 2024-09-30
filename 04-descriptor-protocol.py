class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def __repr__(self) -> str:
        """
        __repr__ is meant to provide an unambiguous string representation of the object.
        It's often used for debugging and should ideally return a string that could be used to
        recreated the object.
        """

        return f"Person(name={self.name!r}, age={self.age})"

    def __str__(self) -> str:
        """
        __str__ is meant to provide a readable string representation of the object.
        It's what gets shown when you print the object or convert it to a string.
        """

        return f"{self.name} is {self.age} years old."


# Creating a Person object
alice = Person(name="Alice", age=30)

# Showing the object representation
print(repr(alice))

# Showing the object
print(alice)
