import function
import PySimpleGUI as sg

# Define the window content
layout = [[sg.Text("Type in a To-Do")],
          [sg.InputText(tooltip="Enter todo"), sg.Button("Add")]]

# Create the window
window = sg.Window("My To-Do App", layout)

# Display the window
window.read()

# Finish up by removing from the screen
window.close()


# # Another way in doing it
# label = sg.Text("Type in a To-Do")
# input_box = sg.InputText(tooltip="Enter todo")
# add_button = sg.Button("Add")
# window = sg.Window("My To-Do App", layout=[[lable, add_button], [input_box]])
