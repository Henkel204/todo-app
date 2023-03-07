from modules import functions

import PySimpleGUI as sg

label = sg.Text("Type in a To-do.")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
b1 = sg.Button("101")
b2 = sg.Button("102")
b3 = sg.Button("103")

# any_text = sg.Text("Just a test!")


window = sg.Window('My To-do App',
                   layout= [[label], [input_box, add_button]],
                   font= ('Helvetica', 20))
'''In the layout each row is a list, that's why we put lists inside a list.'''

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()