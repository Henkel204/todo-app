while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'
            with open('Files/todos_version1.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('Files/todos_version1.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            print("The tasks you chose to do are:")
            with open('Files/todos_version1.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]
            # todos = new_todos

            for index, item in enumerate(todos):
                item = item.title().strip('\n')
                print(f'{index + 1}. {item}')

            # print(f"Length of to do is {len(task_lst)}.")

        case 'edit':
            number = int(input("Number of the todo to edit: "))

            with open('Files/todos_version1.txt', 'r') as file:
                todos = file.readlines()
                todos[number - 1] = input("Enter new todo: ") + '\n'
            with open('Files/todos_version1.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            compl_num = int(input("Number of the task to complete: "))
            index = compl_num - 1

            with open('Files/todos_version1.txt', 'r') as file:
                todos = file.readlines()
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

            with open('Files/todos_version1.txt', 'w') as file:
                file.writelines(todos)

            print(f"Todo {todo_to_remove.capitalize()} was removed from the list.")

        case 'exit':
            break

        case _:
            print("You've entered an invalid command!")

print('Bye')