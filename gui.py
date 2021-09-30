import PySimpleGUI as gui

# settings for buttons
bo = {"size": (5, 2), "font": ("Franklin Gothic", 9), "button_color": ("white", "#6A055F"), "focus": True}
bn = {"size": (5, 2), "font": ("Franklin Gothic", 9), "button_color": ("white", "#BA7185"), "focus": True}
bc = {"size": (5, 2), "font": ("Franklin Gothic", 9), "button_color": ("black", "#FFC300"), "focus": True}

screen = ''

layout = [
    [gui.Text("Not CASIO, but is normal too", size=(30, 1), justification='left', background_color="#31056A",
              font=("Franklin Gothic", 9), text_color="yellow")],
    [gui.Text(screen, size=(16, 1), justification="right", font=("Digital-7", 20), background_color="black",
              text_color="white", key='input')],
    [gui.Button('C', **bo), gui.Button('BS', **bo), gui.Button('√', **bo), gui.Button('%', **bo)],
    [gui.Button('7', **bn), gui.Button('8', **bn), gui.Button('9', **bn), gui.Button('/', **bo)],
    [gui.Button('4', **bn), gui.Button('5', **bn), gui.Button('6', **bn), gui.Button('*', **bo)],
    [gui.Button('1', **bn), gui.Button('2', **bn), gui.Button('3', **bn), gui.Button('-', **bo)],
    [gui.Button('0', **bn), gui.Button('.', **bn), gui.Button('=', **bc), gui.Button('+', **bo)]
]
window = gui.Window("", layout=layout, background_color="#31056A", size=(230, 300))
