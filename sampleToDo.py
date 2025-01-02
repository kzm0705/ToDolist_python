import PySimpleGUI as sg
import os

sg.theme('DarkBrown1')

MAX_TODO = 10  #最大で10個

STATUS = ['未完了','進行中','完了']

todo_list = [[sg.Checkbox("",key=f'-ch{i+1}-',size=(1,1)), sg.Text('',key=f'-todolist{i+1}-',size=(30,1)),
              sg.OptionMenu(STATUS, default_value='未完了',size=(6,1),key=f'-status{i+1}-')] for i in range(MAX_TODO)]

lay_1 = [[sg.Text('just do it !')],
         [sg.Button('追加'),sg.Input(key='-input-', size=(30,1))],
          ]

lay_2 = [[sg.Text('やりたいことリスト',size=(37,1)),sg.Text('ステータス',),sg.Button('削除',key='-delete-',pad=(15,1))],
         [sg.Column(todo_list, key='-todo list-'),],
         ]

layout = [[sg.Frame('group1',lay_1, vertical_alignment='top'),
          sg.Frame('group2', size=(500,500), key='-list-', layout=lay_2)],
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
                window['-input-'].update('')
                break
    if event == '-delete-':
        for i in range(MAX_TODO):
            if window[f'-ch{i+1}-'].get():
                window[f'-todolist{i+1}-'].update('')
                window[f'-ch{i+1}-'].update(False)
                window[f'-status{i+1}-'].update('未完了')


window.close()