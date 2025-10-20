from tkinter import *
from tkinter import font

criador = 'dj_felixo'


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    try:
        global equation_text
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Erro Divisão0")
        equation_text = ''
    except SyntaxError:
        equation_label.set("Erro Syntatic")
        equation_text = ''


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ''


window = Tk()
window.title("Calculadora Pro")
window.geometry("1920x1080")
window.configure(bg="#1e1e2e")
window.resizable(False, False)

equation_text = ""
equation_label = StringVar()

# Fontes personalizadas
display_font = font.Font(family="Arial", size=28, weight="bold")
button_font = font.Font(family="Arial", size=18, weight="bold")

# Display da calculadora
label = Label(
    window, 
    textvariable=equation_label, 
    bg="#2e2e3e", 
    fg="#00ff88",
    width=20, 
    height=2,
    font=display_font,
    anchor="e",
    padx=20,
    pady=20,
    relief=SUNKEN,
    borderwidth=3
)
label.pack(pady=20, padx=20, fill=BOTH)

frame = Frame(window, bg="#1e1e2e")
frame.pack(pady=10)

# Estilo dos botões numéricos
num_style = {
    'height': 3,
    'width': 8,
    'font': button_font,
    'bg': '#3e3e5e',
    'fg': 'white',
    'activebackground': '#5e5e7e',
    'activeforeground': 'white',
    'relief': RAISED,
    'borderwidth': 2
}

# Estilo dos botões de operação
op_style = {
    'height': 3,
    'width': 8,
    'font': button_font,
    'bg': '#ff6b35',
    'fg': 'white',
    'activebackground': '#ff8555',
    'activeforeground': 'white',
    'relief': RAISED,
    'borderwidth': 2
}

# Estilo dos botões especiais
special_style = {
    'height': 3,
    'width': 8,
    'font': button_font,
    'bg': '#6b5eff',
    'fg': 'white',
    'activebackground': '#8b7eff',
    'activeforeground': 'white',
    'relief': RAISED,
    'borderwidth': 2
}

button1 = Button(frame, text='1', command=lambda: button_press(1), **num_style)
button1.grid(row=0, column=0, padx=5, pady=5)

button2 = Button(frame, text='2', command=lambda: button_press(2), **num_style)
button2.grid(row=0, column=1, padx=5, pady=5)

button3 = Button(frame, text='3', command=lambda: button_press(3), **num_style)
button3.grid(row=0, column=2, padx=5, pady=5)

button4 = Button(frame, text='4', command=lambda: button_press(4), **num_style)
button4.grid(row=1, column=0, padx=5, pady=5)

button5 = Button(frame, text='5', command=lambda: button_press(5), **num_style)
button5.grid(row=1, column=1, padx=5, pady=5)

button6 = Button(frame, text='6', command=lambda: button_press(6), **num_style)
button6.grid(row=1, column=2, padx=5, pady=5)

button7 = Button(frame, text='7', command=lambda: button_press(7), **num_style)
button7.grid(row=2, column=0, padx=5, pady=5)

button8 = Button(frame, text='8', command=lambda: button_press(8), **num_style)
button8.grid(row=2, column=1, padx=5, pady=5)

button9 = Button(frame, text='9', command=lambda: button_press(9), **num_style)
button9.grid(row=2, column=2, padx=5, pady=5)

button0 = Button(frame, text='0', command=lambda: button_press(0), **num_style)
button0.grid(row=3, column=0, padx=5, pady=5)

plus = Button(frame, text='+', command=lambda: button_press('+'), **op_style)
plus.grid(row=0, column=3, padx=5, pady=5)

menos = Button(frame, text='-', command=lambda: button_press('-'), **op_style)
menos.grid(row=1, column=3, padx=5, pady=5)

mult = Button(frame, text='×', command=lambda: button_press('*'), **op_style)
mult.grid(row=2, column=3, padx=5, pady=5)

divi = Button(frame, text='÷', command=lambda: button_press('/'), **op_style)
divi.grid(row=3, column=3, padx=5, pady=5)

clear_btn = Button(frame, text='C', command=clear, **special_style)
clear_btn.grid(row=3, column=2, padx=5, pady=5)

deci = Button(frame, text='.', command=lambda: button_press('.'), **num_style)
deci.grid(row=3, column=1, padx=5, pady=5)

# Botão de igual com estilo especial
equal_style = {
    'height': 2,
    'width': 42,
    'font': button_font,
    'bg': '#00ff88',
    'fg': '#1e1e2e',
    'activebackground': '#00dd77',
    'activeforeground': '#1e1e2e',
    'relief': RAISED,
    'borderwidth': 3
}

equal_btn = Button(window, text='=', command=equals, **equal_style)
equal_btn.pack(pady=10, padx=20)
window.mainloop()

print('By: {}'.format(criador))