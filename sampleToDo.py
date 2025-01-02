import PySimpleGUI as sg
import os

sg.theme('DarkBrown1')

MAX_TODO = 10  #最大で10個

todo_list = [[sg.Checkbox("",enable_events=True), sg.Text('',key=f'-todolist{i+1}-'),] for i in range(MAX_TODO)]

lay_1 = [[sg.Text('just do it !')],
         [sg.Button('追加'),sg.Input(key='-input-', size=(30,1))],
          ]

lay_2 = [[sg.Text('やりたいことリスト')],
         [sg.Column(todo_list, key='-todo list-'),]]

layout = [[sg.Frame('group1',lay_1, vertical_alignment='top'),
          sg.Frame('group2', size=(500,500), key='-list-', layout=lay_2)]
           ]


window = sg.Window('TO DO application', layout)

while True:
    event, value = window.read(timeout=100)

    if event == sg.WIN_CLOSED:
        break
    if event == '追加':
        do = window['-input-'].get()
        for i in range(MAX_TODO):
            if window[f'-todolist{i+1}-'].get() == '':
                window[f'-todolist{i+1}-'].update(do)
                break


window.close()