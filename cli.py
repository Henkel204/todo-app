# from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        print("The tasks you chose to do are:")

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        # todos = new_todos

        for index, item in enumerate(todos):
            item = item.title().strip('\n')
            print(f'{index + 1}. {item}')

        # print(f"Length of to do is {len(task_lst)}.")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            todos[number - 1] = input("Enter new todo: ") + '\n'
            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue  # it will run another cycle of the while loop

    elif user_action.startswith('complete'):
        try:
            compl_num = int(user_action[9:])
            index = compl_num - 1

            todos = functions.get_todos()
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"Todo {todo_to_remove.capitalize()} was removed from the list.")
        except IndexError:
            print(f'Enter a number up to {len(todos)}.')
            continue  # it will run another cycle of the while loop

    elif user_action.startswith('exit'):
        print('Bye')
        break

    else:
        print("You've entered an invalid command!")
