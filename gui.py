from modules import functions
import time
import PySimpleGUI as sg

sg.theme("DarkPurple6")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a To-do.")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
b1 = sg.Button("101")
b2 = sg.Button("102")
b3 = sg.Button("103")

# any_text = sg.Text("Just a test!")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My To-do App', layout=layout,
                   font=('Helvetica', 20))
'''In the layout each row is a list, that's why we put lists inside a list.'''

while True:
    event, values = window.read(timeout=400)  # allows the while loop to run every 10 miliseconds
    # and as a result to update the time
    window["clock"].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    # print(event) we print these only if we want to see what exactly happens
    # print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select and item first!", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select and item first!", font=("Helvetica", 20))

        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
