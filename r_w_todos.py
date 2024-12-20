FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list
    of todo items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """Write a list of todo items to a text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)
