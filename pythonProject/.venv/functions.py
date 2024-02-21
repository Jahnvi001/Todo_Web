FILEPATH = 'todos.txt'


def get_to_dos(filepath=FILEPATH):
    """Read a text file and returns the list of to-do items."""
    with open(filepath, 'r') as file_l:
        to_dos_l = file_l.readlines()
        return to_dos_l


def write_to_dos(to_dos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(to_dos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_to_dos())