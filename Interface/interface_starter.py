from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout= [
    [sg.Text('User'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*')],
    [sg.Checkbox('Lembrar de mim?')],
    [sg.Button('Entrar')],
    
]

janela = sg.Window('Tela de Log-in',layout)


while True:
    enventos, valores =janela.read()
    if enventos == sg.WINDOW_CLOSED:
        break
    if enventos == 'Entrar':
        if valores['usuario']== 'jao' and valores ['senha']=='000000':
            print("Bem Vindo")