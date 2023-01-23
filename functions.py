FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Use to read files and return list to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    use to write item in todos file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
