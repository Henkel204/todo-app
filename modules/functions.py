def get_todos(filepath='/Users/georgi/Documents/App1/Files/todos.txt'):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath='/Users/georgi/Documents/App1/Files/todos.txt'):
    """ Write a to-do items list into a text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    # the function doesn't return anything; it only stores the todos in the file


if __name__ == "__main__":
    """This will run only if you run functions from here.
    This is it's main directory. When you import it elsewhere, this
    part of the program will not run"""
    print("Hello!")
    print(get_todos())
