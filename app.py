from gui import window, screen


while True:
    button, values = window.read()

    if button == "C":
        screen = ""
        window.FindElement('input').Update(screen)
    elif button == "BS":
        screen = screen[:-1]
        window.FindElement("input").Update(screen)
    elif button in ["Quit", None]:
        break
    elif button == "=":
        try:
            answer = eval(screen)
            answer = str(round(float(answer), 5))
            window.FindElement("input").Update(answer)
            screen = answer
        except ZeroDivisionError:
            screen = "ERROR"
            window.FindElement("input").Update(screen)
        except NameError:
            screen = ""
            window.FindElement("input").Update(screen)
    elif button == "√":
        screen = str(float(screen) ** 0.5)
        window.FindElement('input').Update(screen)
    elif button == "%":
        screen = str(float(screen) / 100)
        window.FindElement('input').Update(screen)
    else:
        screen += button
        window.FindElement('input').Update(screen)