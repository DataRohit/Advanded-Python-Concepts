# Dynamic code execution in Python using exec
def demonstrate_exec():
    # The exec function can be used to execute code dynamically
    code = """def greet(name):
    return f'Hello, {name}!'"""

    # Dictionary to store the local scope of the executed code
    local_scope = {}

    # Execute the code in the local scope
    exec(code, {}, local_scope)

    # Print the result of the executed code
    print(local_scope["greet"]("world"))


# Dynamic code execution in Python using eval
def demonstrate_eval():
    # Take user input for an expression
    expressions = input("Type an expression: ")

    # Calculate the result of the expression
    result = eval(expressions)

    # Print the result of the expression
    print(f"Result of eval: {result}\n")


# Dynamic code execution in Python using eval with locals and globals
def demonstrate_safe_eval():
    # Take user input for an expression
    expressions = input("Type an expression: ")

    # Initialize a dictionary with variables
    variables = {"a": 1, "b": 2, "c": 3}

    # Calculate the result of the expression using the variables
    result = eval(expressions, {}, variables)

    # Print the result of the expression
    print(f"Result of safe eval: {result}\n")


# demonstrate_exec()
# demonstrate_eval()
demonstrate_safe_eval()
