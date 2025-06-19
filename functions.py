FILEPATH = "todoList.txt"


def get_todolist(filepath = FILEPATH):
    """Reads a default text file and returns the
    to-do items in a list
    """
    with open(filepath, 'r') as file_local:
        todolist_local = file_local.readlines()
    return todolist_local

def write_todolist(todolist_arg, filepath = FILEPATH):
    """Takes the to-do list as a mandatory argument
    and writes the items of that list in a default
    text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todolist_arg)
    return None

if __name__ == "__main__":
    print("Hello:functions")
