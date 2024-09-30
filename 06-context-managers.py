class FileManager(object):
    # Constructor to initialize the filename and mode
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    # Method to open the file and return the file object
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    # Method to close the file and handle the exceptions
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

        if exc_type is not None:
            print(f"An error occurred: {exc_val}")
        return True


if __name__ == "__main__":
    # Use the custom file manager to open the file in write mode
    with FileManager("test.txt", "w") as f:
        # Write the content and print the message
        f.write("Hello, World!")
        print("File written successfully")

    # Use the custom file manager to open the file in read mode
    with FileManager("test.txt", "r") as f:
        # Write the content and print the message
        content = f.read()
        print("File content:", content)
