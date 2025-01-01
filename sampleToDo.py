import PySimpleGUI as sg
import os

sg.theme('DarkBrown1')

MAX_TODO = 10 * 2

list_todo = [[sg.Text('', key='=output=')] for i in range(10 + 1)]

def todo_input(text):
    list_todo.append([text])



lay_1 = [[sg.Text('just do it !')],
         [sg.Button('追加'),sg.Input(key='-input-', size=(30,1))],
          ]

lay_2 = [[sg.Text('やりたいことリスト')],
         [sg.Text('', key='-output-')]]

layout = [[sg.Frame('group1',lay_1, vertical_alignment='top'),
           sg.Frame('', size=(500,500), layout= lay_2, key='-list-')],
           ]


window = sg.Window('TO DO application', layout)

while True:
    event, value = window.read(timeout=100)

    if event == sg.WIN_CLOSED:
        break
    if event == '追加':
        do = window['-input-'].get()
        window['-output-'].update(do)

window.close()