from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkGrey6')
layout= [
    [sg.Text('Primeiro Valor:'),sg.InputText()],
    [sg.Text('Segundo Valor:'),sg.InputText()],
    [sg.OptionMenu(default_value ='+',values=('+','-', '/', '*'),key='operacao')],
    [sg.Button('Calcular')],
    [sg.Text('Resultado apresentado no terminal. (por enquanto)')]
    
    
]

janela = sg.Window('Calculadora',layout)



while True:
    envetos, valores =janela.read()
    if envetos == sg.WINDOW_CLOSED:
        break
    if envetos == 'Calcular':
        if valores['operacao']== '+':
            x=float(valores[0]) 
            y=float(valores[1])
            print(x+y)
        if valores['operacao']== '-':
            x=float(valores[0]) 
            y=float(valores[1])
            print(x-y)
        if valores['operacao']== '/':
            x=float(valores[0]) 
            y=float(valores[1])
            print(x/y)
        if valores['operacao']== '*':
            x=float(valores[0]) 
            y=float(valores[1])
            print(x*y)