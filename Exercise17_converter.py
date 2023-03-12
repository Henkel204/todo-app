import PySimpleGUI as g


from modules.converters import convert

label1 = g.Text("Enter feet:")
label2 = g.Text("Enter inches:")
input_feet = g.InputText(key="feet")
input_inches = g.InputText(key="inches")
convert_button = g.Button("Convert")
output_label = g.Text("", key="output")
layout = [[label1, input_feet], [label2, input_inches], [convert_button, output_label]]

window = g.Window("Convertor", layout=layout, font=('Helvetica', 20))

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()