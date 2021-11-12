# Caeserplus Demo
# Owner: awesomelewis2007
# Co-Owner: WolfieBoy
import sys
def demo():
    import PySimpleGUI as sg
    import sys

    sg.theme('black')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Enter a piece of data to corrupt')],
                [sg.Text('Data:'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Quit')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
            window.close()
            sys.exit()
        if event == 'Ok':
            window.close()
            break
    return values[0]
def output_message(values):
    import caeserplus
    import PySimpleGUI as sg
    import sys
    key,output = caeserplus.encode(values)
    sg.theme('Green')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text("Command completed successfully")],
                [sg.Text("Key:"+str(key))],
                [sg.Text("Output:"+output)],
                [sg.Button('Ok'), sg.Button('Quit')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    print(key)
    print(output)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit' or event == 'Ok': # if user closes window or clicks cancel
            break

    window.close()
def error(value):
    import PySimpleGUI as sg
    import sys
    sg.theme('black')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text("Error in demo module")],
                [sg.Text(value)],
    ]

    # Create the Window
    window = sg.Window('Error', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit' or event == 'Ok': # if user closes window or clicks cancel
            break

    window.close()
value = demo()
if value == "":
    error("Please enter data to encrypt!")
    sys.exit()
output_message(value)