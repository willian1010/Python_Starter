import PySimpleGUI as sg
import random as r 

sg.theme('darkgray6')
layout=[
    
    [sg.Text('Tamanho do Dado: (D:?)'), sg.InputText()],    
    [sg.Button('Rolar')]    
    ]
window = sg.Window('Dado',layout)

while True :
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Rolar':
     y = int(values[0])
     x = r.randint(1,y)
     
     
     sg.popup(x)
     
     