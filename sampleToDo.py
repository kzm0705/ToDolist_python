import PySimpleGUI as sg


sg.theme('DarkBrown1')

MAX_TODO = 10  #最大で10個

STATUS = ['未完了','進行中','完了']

SAVE_DATA = ['保存','読み込み']

todo_list = [[sg.Checkbox("",key=f'-ch{i+1}-',size=(1,1),), sg.Text('', key=f'-todolist{i+1}-',size=(27,1)),
              sg.OptionMenu(STATUS, default_value='未完了',size=(6,1), key=f'-status{i+1}-',)] for i in range(MAX_TODO)]

lay_1 = [[sg.Text('just do it !')],
         [sg.Button('追加'),sg.Input(key='-input-', size=(30,1))],
          ]

lay_2 = [[sg.Text('やりたいことリスト',size=(15,1)),sg.ButtonMenu('ファイル',['sevemenu',SAVE_DATA],pad=(30,1),key='-filesave-'),
          sg.Text('ステータス',pad=(25,10)),sg.Button('削除',key='-delete-',pad=(15,1))],
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
        
    if event == '-filesave-':
        if value['-filesave-'] == '保存':
             with open('todo.txt', 'w', encoding='utf-8') as f:
                for i in range(10):
                    if window[f'-todolist{i+1}-'] != "":
                        do = window[f'-todolist{i+1}-'].get()
                        status = value[f'-status{i+1}-']
                        f.write(f'{do},{status}\n')
        if value['-filesave-'] == '読み込み':
            with open('todo.txt', 'r', encoding='utf-8') as f:
                for i, line in enumerate(f):
                    do, status = line.strip().split(',')
                    window[f'-todolist{i+1}-'].update(do)
                    window[f'-status{i+1}-'].update(status)


window.close()