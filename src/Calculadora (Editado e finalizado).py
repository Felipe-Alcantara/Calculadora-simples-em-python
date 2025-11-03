from tkinter import *
from tkinter import font, ttk
from datetime import datetime
import math
import json
import os

criador = 'dj_felixo'

# Lista para armazenar o histórico
history = []

# Arquivo para salvar histórico
HISTORY_FILE = "calculator_history.json"

# Variável global para o tema atual
current_theme = "dark"

# Definição dos temas
themes = {
    "dark": {
        "bg_main": "#1e1e2e",
        "bg_secondary": "#2e2e3e",
        "bg_tertiary": "#3e3e5e",
        "fg_primary": "#1abc9c",
        "fg_secondary": "#ecf0f1",
        "fg_tertiary": "#95a5a6",
        "btn_num": "#3e3e5e",
        "btn_num_hover": "#5e5e7e",
        "btn_op": "#ff6b35",
        "btn_op_hover": "#ff8555",
        "btn_special": "#6b5eff",
        "btn_special_hover": "#8b7eff",
        "btn_sci": "#2ecc71",
        "btn_sci_hover": "#27ae60",
        "btn_equal": "#1abc9c",
        "btn_equal_fg": "#1e1e2e",
        "btn_rule": "#9b59b6",
        "border": "#3e3e5e"
    },
    "light": {
        "bg_main": "#f5f5f5",
        "bg_secondary": "#ffffff",
        "bg_tertiary": "#e0e0e0",
        "fg_primary": "#2c3e50",
        "fg_secondary": "#34495e",
        "fg_tertiary": "#7f8c8d",
        "btn_num": "#ecf0f1",
        "btn_num_hover": "#bdc3c7",
        "btn_op": "#e74c3c",
        "btn_op_hover": "#c0392b",
        "btn_special": "#3498db",
        "btn_special_hover": "#2980b9",
        "btn_sci": "#27ae60",
        "btn_sci_hover": "#229954",
        "btn_equal": "#2ecc71",
        "btn_equal_fg": "#ffffff",
        "btn_rule": "#9b59b6",
        "border": "#bdc3c7"
    }
}


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def scientific_operation(operation):
    """Executa operações científicas"""
    global equation_text
    try:
        if equation_text:
            current_value = float(eval(equation_text.replace('×', '*').replace('÷', '/')))
            original = equation_text
            
            if operation == 'sqrt':
                result = math.sqrt(current_value)
                calc_display = f"√({original})"
            elif operation == 'square':
                result = current_value ** 2
                calc_display = f"({original})²"
            elif operation == 'power':
                equation_text = equation_text + "**"
                equation_label.set(equation_text)
                return
            elif operation == 'percent':
                result = current_value / 100
                calc_display = f"{original}%"
            elif operation == 'inverse':
                result = 1 / current_value
                calc_display = f"1/({original})"
            elif operation == 'sin':
                result = math.sin(math.radians(current_value))
                calc_display = f"sin({original}°)"
            elif operation == 'cos':
                result = math.cos(math.radians(current_value))
                calc_display = f"cos({original}°)"
            elif operation == 'tan':
                result = math.tan(math.radians(current_value))
                calc_display = f"tan({original}°)"
            elif operation == 'log':
                result = math.log10(current_value)
                calc_display = f"log({original})"
            elif operation == 'ln':
                result = math.log(current_value)
                calc_display = f"ln({original})"
            else:
                return
            
            result_str = str(result)
            add_to_history(calc_display, result_str)
            equation_text = result_str
            equation_label.set(result_str)
    except ValueError as e:
        equation_label.set("Erro: Valor inválido")
        equation_text = ''
    except ZeroDivisionError:
        equation_label.set("Erro: Divisão por 0")
        equation_text = ''
    except Exception as e:
        equation_label.set("Erro")
        equation_text = ''


def insert_constant(constant):
    """Insere constantes matemáticas"""
    global equation_text
    if constant == 'pi':
        equation_text = equation_text + str(math.pi)
    elif constant == 'e':
        equation_text = equation_text + str(math.e)
    equation_label.set(equation_text)


def add_to_history(calculation, result):
    """Adiciona um cálculo ao histórico"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    history_entry = f"{timestamp} | {calculation} = {result}"
    history.append(history_entry)
    update_history_display()
    save_history()


def save_history():
    """Salva o histórico em arquivo JSON"""
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Erro ao salvar histórico: {e}")


def load_history():
    """Carrega o histórico do arquivo JSON"""
    global history
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)
                update_history_display()
    except Exception as e:
        print(f"Erro ao carregar histórico: {e}")
        history = []


def update_history_display():
    """Atualiza a exibição do histórico"""
    history_text.config(state=NORMAL)
    history_text.delete(1.0, END)
    
    if not history:
        history_text.insert(END, "Nenhum cálculo ainda...\n", "empty")
    else:
        for i, calc in enumerate(reversed(history), 1):
            history_text.insert(END, f"{calc}\n", "calculation")
    
    history_text.config(state=DISABLED)
    history_text.see(END)


def clear_history():
    """Limpa todo o histórico"""
    global history
    history = []
    update_history_display()
    save_history()


def export_history():
    """Exporta o histórico para um arquivo de texto"""
    try:
        if not history:
            return
        
        filename = f"historico_calculadora_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 50 + "\n")
            f.write("HISTÓRICO DA CALCULADORA CIENTÍFICA PRO\n")
            f.write("=" * 50 + "\n\n")
            for calc in history:
                f.write(f"{calc}\n")
            f.write("\n" + "=" * 50 + "\n")
            f.write(f"Total de cálculos: {len(history)}\n")
            f.write(f"By: {criador}\n")
        
        # Mensagem de sucesso
        from tkinter import messagebox
        messagebox.showinfo("Sucesso", f"Histórico exportado para:\n{filename}")
    except Exception as e:
        from tkinter import messagebox
        messagebox.showerror("Erro", f"Erro ao exportar histórico:\n{e}")


def equals():
    try:
        global equation_text
        if equation_text:
            # Salva a expressão original antes de calcular
            original_expression = equation_text
            
            # Substitui símbolos para cálculo
            calc_expression = equation_text.replace('×', '*').replace('÷', '/')
            total = str(eval(calc_expression))
            
            # Adiciona ao histórico com símbolos bonitos
            display_expression = original_expression.replace('*', '×').replace('/', '÷')
            add_to_history(display_expression, total)
            
            equation_label.set(total)
            equation_text = total
    except ZeroDivisionError:
        equation_label.set("Erro: Divisão por 0")
        equation_text = ''
    except SyntaxError:
        equation_label.set("Erro: Sintaxe inválida")
        equation_text = ''
    except Exception:
        equation_label.set("Erro")
        equation_text = ''


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ''


def toggle_theme():
    """Alterna entre tema claro e escuro"""
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    apply_theme()


def apply_theme():
    """Aplica o tema atual a todos os elementos"""
    theme = themes[current_theme]
    
    # Janela principal
    window.configure(bg=theme["bg_main"])
    
    # Container principal
    main_container.configure(bg=theme["bg_main"])
    
    # Frame da calculadora
    calculator_frame.configure(bg=theme["bg_main"])
    
    # Display
    label.configure(
        bg=theme["bg_secondary"],
        fg=theme["fg_primary"],
        borderwidth=3
    )
    
    # Frame dos botões numéricos
    frame.configure(bg=theme["bg_main"])
    sci_frame.configure(bg=theme["bg_main"])
    
    # Histórico
    history_frame.configure(bg=theme["bg_secondary"])
    history_title.configure(bg=theme["bg_secondary"], fg=theme["fg_primary"])
    history_scroll_frame.configure(bg=theme["bg_secondary"])
    history_text.configure(
        bg=theme["bg_main"],
        fg=theme["fg_secondary"],
        insertbackground=theme["fg_primary"]
    )
    
    # Atualiza tags do histórico
    history_text.tag_config("calculation", foreground=theme["fg_secondary"])
    history_text.tag_config("empty", foreground="#95a5a6", justify=CENTER)
    
    clear_history_btn.configure(bg=theme["btn_op"], activebackground=theme["btn_op_hover"])
    export_history_btn.configure(bg="#3498db", activebackground="#2980b9")
    
    # Atualiza cores dos botões numéricos
    for widget in frame.winfo_children():
        if isinstance(widget, Button):
            btn_text = widget.cget("text")
            if btn_text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                widget.configure(
                    bg=theme["btn_num"],
                    fg=theme["fg_secondary"],
                    activebackground=theme["btn_num_hover"]
                )
            elif btn_text in ['+', '-', '×', '÷']:
                widget.configure(
                    bg=theme["btn_op"],
                    activebackground=theme["btn_op_hover"]
                )
            elif btn_text == 'C':
                widget.configure(
                    bg=theme["btn_special"],
                    activebackground=theme["btn_special_hover"]
                )
    
    # Atualiza botões científicos
    for widget in sci_frame.winfo_children():
        if isinstance(widget, Button):
            widget.configure(
                bg=theme["btn_sci"],
                activebackground=theme["btn_sci_hover"]
            )
    
    # Botão igual
    equal_btn.configure(
        bg=theme["btn_equal"],
        fg=theme["btn_equal_fg"],
        activebackground=theme["btn_sci_hover"]
    )
    
    # Botão regra de 3
    rule_btn.configure(
        bg=theme["btn_rule"],
        activebackground="#8e44ad"
    )
    
    # Botão de tema
    theme_icon = "🌙" if current_theme == "light" else "☀️"
    theme_text = "Modo Escuro" if current_theme == "light" else "Modo Claro"
    theme_btn.configure(text=f"{theme_icon} {theme_text}")


window = Tk()
window.title("Calculadora Científica Pro")
window.geometry("1150x750")
window.configure(bg="#1e1e2e")
window.resizable(False, False)

equation_text = ""
equation_label = StringVar()

# Fontes personalizadas
display_font = font.Font(family="Arial", size=28, weight="bold")
button_font = font.Font(family="Arial", size=18, weight="bold")
history_font = font.Font(family="Consolas", size=10)

# Container principal
main_container = Frame(window, bg="#1e1e2e")
main_container.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Frame esquerdo - Calculadora
calculator_frame = Frame(main_container, bg="#1e1e2e")
calculator_frame.pack(side=LEFT, padx=(0, 10))

# Frame direito - Histórico
history_frame = Frame(main_container, bg="#2e2e3e", relief=RAISED, borderwidth=2)
history_frame.pack(side=RIGHT, fill=BOTH, expand=True)

# Título do histórico
history_title = Label(
    history_frame,
    text="📜 Histórico de Cálculos",
    bg="#2e2e3e",
    fg="#00ff88",
    font=font.Font(family="Arial", size=14, weight="bold"),
    pady=10
)
history_title.pack(fill=X)

# Área de texto do histórico com scrollbar
history_scroll_frame = Frame(history_frame, bg="#2e2e3e")
history_scroll_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

history_scrollbar = Scrollbar(history_scroll_frame)
history_scrollbar.pack(side=RIGHT, fill=Y)

history_text = Text(
    history_scroll_frame,
    bg="#1e1e2e",
    fg="#ffffff",
    font=history_font,
    wrap=WORD,
    state=DISABLED,
    yscrollcommand=history_scrollbar.set,
    relief=SUNKEN,
    borderwidth=2,
    padx=10,
    pady=10
)
history_text.pack(side=LEFT, fill=BOTH, expand=True)
history_scrollbar.config(command=history_text.yview)

# Tags de estilo para o histórico
history_text.tag_config("calculation", foreground="#ecf0f1")
history_text.tag_config("empty", foreground="#95a5a6", justify=CENTER)

# Frame para botões do histórico
history_buttons_frame = Frame(history_frame, bg="#1e1e2e")
history_buttons_frame.pack(fill=X, padx=5, pady=5)

# Botão para limpar histórico
clear_history_btn = Button(
    history_buttons_frame,
    text="🗑️ Limpar",
    command=clear_history,
    bg="#ff6b35",
    fg="white",
    font=font.Font(family="Arial", size=10, weight="bold"),
    relief=RAISED,
    borderwidth=2,
    pady=5,
    cursor="hand2"
)
clear_history_btn.pack(side=LEFT, fill=X, expand=True, padx=(0, 3))

# Botão para exportar histórico
export_history_btn = Button(
    history_buttons_frame,
    text="💾 Exportar",
    command=export_history,
    bg="#3498db",
    fg="white",
    font=font.Font(family="Arial", size=10, weight="bold"),
    relief=RAISED,
    borderwidth=2,
    pady=5,
    cursor="hand2"
)
export_history_btn.pack(side=RIGHT, fill=X, expand=True, padx=(3, 0))

# Display da calculadora
label = Label(
    calculator_frame, 
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
label.pack(pady=(0, 20))

frame = Frame(calculator_frame, bg="#1e1e2e")
frame.pack()

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

# Estilo dos botões científicos
sci_style = {
    'height': 2,
    'width': 6,
    'font': font.Font(family="Arial", size=12, weight="bold"),
    'bg': '#2ecc71',
    'fg': 'white',
    'activebackground': '#27ae60',
    'activeforeground': 'white',
    'relief': RAISED,
    'borderwidth': 2
}

# Frame para botões científicos (acima dos botões numéricos)
sci_frame = Frame(calculator_frame, bg="#1e1e2e")
sci_frame.pack(pady=(0, 10))

# Linha 1 de funções científicas
Button(sci_frame, text='√', command=lambda: scientific_operation('sqrt'), **sci_style).grid(row=0, column=0, padx=3, pady=3)
Button(sci_frame, text='x²', command=lambda: scientific_operation('square'), **sci_style).grid(row=0, column=1, padx=3, pady=3)
Button(sci_frame, text='xʸ', command=lambda: scientific_operation('power'), **sci_style).grid(row=0, column=2, padx=3, pady=3)
Button(sci_frame, text='%', command=lambda: scientific_operation('percent'), **sci_style).grid(row=0, column=3, padx=3, pady=3)
Button(sci_frame, text='1/x', command=lambda: scientific_operation('inverse'), **sci_style).grid(row=0, column=4, padx=3, pady=3)

# Linha 2 de funções científicas
Button(sci_frame, text='sin', command=lambda: scientific_operation('sin'), **sci_style).grid(row=1, column=0, padx=3, pady=3)
Button(sci_frame, text='cos', command=lambda: scientific_operation('cos'), **sci_style).grid(row=1, column=1, padx=3, pady=3)
Button(sci_frame, text='tan', command=lambda: scientific_operation('tan'), **sci_style).grid(row=1, column=2, padx=3, pady=3)
Button(sci_frame, text='log', command=lambda: scientific_operation('log'), **sci_style).grid(row=1, column=3, padx=3, pady=3)
Button(sci_frame, text='ln', command=lambda: scientific_operation('ln'), **sci_style).grid(row=1, column=4, padx=3, pady=3)

# Linha 3 - Constantes
Button(sci_frame, text='π', command=lambda: insert_constant('pi'), **sci_style).grid(row=2, column=0, padx=3, pady=3)
Button(sci_frame, text='e', command=lambda: insert_constant('e'), **sci_style).grid(row=2, column=1, padx=3, pady=3)
Button(sci_frame, text='(', command=lambda: button_press('('), **sci_style).grid(row=2, column=2, padx=3, pady=3)
Button(sci_frame, text=')', command=lambda: button_press(')'), **sci_style).grid(row=2, column=3, padx=3, pady=3)
Button(sci_frame, text='←', command=lambda: backspace(), **sci_style).grid(row=2, column=4, padx=3, pady=3)


def backspace():
    """Remove o último caractere"""
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text if equation_text else "")


def open_rule_of_three():
    """Abre janela de Regra de 3"""
    rule_window = Toplevel(window)
    rule_window.title("Regra de 3 Simples")
    rule_window.geometry("500x450")
    rule_window.configure(bg="#1e1e2e")
    rule_window.resizable(False, False)
    
    # Título
    title = Label(
        rule_window,
        text="📐 Regra de 3 Simples",
        bg="#1e1e2e",
        fg="#00ff88",
        font=font.Font(family="Arial", size=18, weight="bold"),
        pady=15
    )
    title.pack()
    
    # Frame principal
    main_frame = Frame(rule_window, bg="#1e1e2e")
    main_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)
    
    # Explicação
    explanation = Label(
        main_frame,
        text="Se A está para B, então C está para X\n(A/B = C/X)",
        bg="#2e2e3e",
        fg="#ffffff",
        font=font.Font(family="Arial", size=11),
        pady=10,
        relief=RAISED,
        borderwidth=2
    )
    explanation.pack(fill=X, pady=(0, 20))
    
    # Frame dos inputs
    input_frame = Frame(main_frame, bg="#1e1e2e")
    input_frame.pack(pady=10)
    
    # Estilo dos labels e entries
    label_style = {
        'bg': '#1e1e2e',
        'fg': '#00ff88',
        'font': font.Font(family="Arial", size=13, weight="bold")
    }
    
    entry_style = {
        'font': font.Font(family="Arial", size=12),
        'bg': '#2e2e3e',
        'fg': '#00ff88',
        'insertbackground': '#00ff88',
        'relief': SUNKEN,
        'borderwidth': 2,
        'width': 15
    }
    
    # Linha 1: A está para B
    Label(input_frame, text="A:", **label_style).grid(row=0, column=0, sticky=E, padx=5, pady=10)
    entry_a = Entry(input_frame, **entry_style)
    entry_a.grid(row=0, column=1, padx=5, pady=10)
    
    Label(input_frame, text=" está para ", bg="#1e1e2e", fg="#ffffff", 
          font=font.Font(family="Arial", size=11)).grid(row=0, column=2, padx=5)
    
    Label(input_frame, text="B:", **label_style).grid(row=0, column=3, sticky=E, padx=5, pady=10)
    entry_b = Entry(input_frame, **entry_style)
    entry_b.grid(row=0, column=4, padx=5, pady=10)
    
    # Separador
    Label(input_frame, text="═══════════════", bg="#1e1e2e", fg="#6b5eff",
          font=font.Font(family="Arial", size=14)).grid(row=1, column=0, columnspan=5, pady=5)
    
    # Linha 2: C está para X
    Label(input_frame, text="C:", **label_style).grid(row=2, column=0, sticky=E, padx=5, pady=10)
    entry_c = Entry(input_frame, **entry_style)
    entry_c.grid(row=2, column=1, padx=5, pady=10)
    
    Label(input_frame, text=" está para ", bg="#1e1e2e", fg="#ffffff",
          font=font.Font(family="Arial", size=11)).grid(row=2, column=2, padx=5)
    
    Label(input_frame, text="X:", **label_style).grid(row=2, column=3, sticky=E, padx=5, pady=10)
    result_var = StringVar()
    result_var.set("?")
    result_label = Label(
        input_frame,
        textvariable=result_var,
        bg="#2e2e3e",
        fg="#00ff88",
        font=font.Font(family="Arial", size=14, weight="bold"),
        width=12,
        height=1,
        relief=SUNKEN,
        borderwidth=2,
        anchor=CENTER
    )
    result_label.grid(row=2, column=4, padx=5, pady=10)
    
    # Frame dos botões
    button_frame = Frame(main_frame, bg="#1e1e2e")
    button_frame.pack(pady=20)
    
    def calculate_rule():
        """Calcula a regra de 3"""
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            
            # Fórmula: X = (B × C) / A
            x = (b * c) / a
            
            result_var.set(f"{x:.4f}")
            
            # Adiciona ao histórico da calculadora principal
            calc_text = f"Regra de 3: {a}→{b} :: {c}→X"
            add_to_history(calc_text, f"{x:.4f}")
            
        except ValueError:
            result_var.set("Erro: Valor inválido")
        except ZeroDivisionError:
            result_var.set("Erro: A ≠ 0")
        except Exception:
            result_var.set("Erro")
    
    def clear_fields():
        """Limpa todos os campos"""
        entry_a.delete(0, END)
        entry_b.delete(0, END)
        entry_c.delete(0, END)
        result_var.set("?")
        entry_a.focus()
    
    # Botão Calcular
    btn_calc = Button(
        button_frame,
        text="🔢 Calcular",
        command=calculate_rule,
        bg="#00ff88",
        fg="#1e1e2e",
        font=font.Font(family="Arial", size=13, weight="bold"),
        width=15,
        height=2,
        relief=RAISED,
        borderwidth=3,
        cursor="hand2"
    )
    btn_calc.pack(side=LEFT, padx=10)
    
    # Botão Limpar
    btn_clear = Button(
        button_frame,
        text="🗑️ Limpar",
        command=clear_fields,
        bg="#ff6b35",
        fg="white",
        font=font.Font(family="Arial", size=13, weight="bold"),
        width=15,
        height=2,
        relief=RAISED,
        borderwidth=3,
        cursor="hand2"
    )
    btn_clear.pack(side=LEFT, padx=10)
    
    # Exemplo
    example = Label(
        main_frame,
        text="Exemplo: Se 2 kg custam 10 reais, quanto custam 5 kg?\nA=2, B=10, C=5 → X=25",
        bg="#2e2e3e",
        fg="#8e8e9e",
        font=font.Font(family="Arial", size=9, style="italic"),
        pady=8,
        relief=SUNKEN,
        borderwidth=1
    )
    example.pack(fill=X, pady=(10, 0))
    
    # Foco inicial
    entry_a.focus()
    
    # Bind Enter key
    def on_enter(event):
        calculate_rule()
    
    entry_a.bind('<Return>', on_enter)
    entry_b.bind('<Return>', on_enter)
    entry_c.bind('<Return>', on_enter)

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

equal_btn = Button(calculator_frame, text='=', command=equals, **equal_style)
equal_btn.pack(pady=10)

# Botão Regra de 3
rule_btn_style = {
    'height': 1,
    'font': font.Font(family="Arial", size=11, weight="bold"),
    'bg': '#9b59b6',
    'fg': 'white',
    'activebackground': '#8e44ad',
    'activeforeground': 'white',
    'relief': RAISED,
    'borderwidth': 2,
    'cursor': 'hand2'
}

rule_btn = Button(calculator_frame, text='📐 Regra de 3', command=open_rule_of_three, **rule_btn_style)
rule_btn.pack(pady=(0, 10), fill=X, padx=10)

# Botão de Tema
theme_btn_style = {
    'height': 1,
    'font': font.Font(family="Arial", size=11, weight="bold"),
    'bg': '#34495e',
    'fg': 'white',
    'activebackground': '#2c3e50',
    'activeforeground': 'white',
    'relief': RAISED,
    'borderwidth': 2,
    'cursor': 'hand2'
}

theme_btn = Button(calculator_frame, text='☀️ Modo Claro', command=toggle_theme, **theme_btn_style)
theme_btn.pack(pady=(0, 10), fill=X, padx=10)

# Carrega o histórico salvo e inicializa a exibição
load_history()

window.mainloop()

print('By: {}'.format(criador))