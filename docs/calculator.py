"""
Calculadora Pro - Versão Brython
By: dj_felixo
"""

from browser import document, html

# Variável global para armazenar a equação
equation_text = ""


def button_press(num):
    """Adiciona um número ou operador ao display"""
    global equation_text
    equation_text = equation_text + str(num)
    update_display()


def equals(ev):
    """Calcula o resultado da equação"""
    global equation_text
    try:
        # Substitui os símbolos visuais pelos operadores Python
        calc_text = equation_text.replace('×', '*').replace('÷', '/')
        total = str(eval(calc_text))
        equation_text = total
        update_display()
    except ZeroDivisionError:
        document["display"].text = "Erro: Divisão por 0"
        equation_text = ""
    except SyntaxError:
        document["display"].text = "Erro: Sintaxe inválida"
        equation_text = ""
    except Exception as e:
        document["display"].text = "Erro"
        equation_text = ""


def clear(ev):
    """Limpa o display"""
    global equation_text
    equation_text = ""
    update_display()


def update_display():
    """Atualiza o display com o texto atual"""
    if equation_text == "":
        document["display"].text = "0"
    else:
        document["display"].text = equation_text


def setup_calculator():
    """Configura os event listeners dos botões"""
    
    # Botões numéricos
    for i in range(10):
        btn = document[f"btn-{i}"]
        btn.bind("click", lambda ev, num=i: button_press(num))
    
    # Botão de ponto decimal
    document["btn-dot"].bind("click", lambda ev: button_press('.'))
    
    # Botões de operação
    document["btn-plus"].bind("click", lambda ev: button_press('+'))
    document["btn-minus"].bind("click", lambda ev: button_press('-'))
    document["btn-mult"].bind("click", lambda ev: button_press('×'))
    document["btn-div"].bind("click", lambda ev: button_press('÷'))
    
    # Botões especiais
    document["btn-equal"].bind("click", equals)
    document["btn-clear"].bind("click", clear)
    
    # Suporte para teclado
    def handle_keypress(ev):
        key = ev.key
        
        # Números e ponto
        if key in '0123456789.':
            button_press(key)
        # Operadores
        elif key == '+':
            button_press('+')
        elif key == '-':
            button_press('-')
        elif key == '*':
            button_press('×')
        elif key == '/':
            ev.preventDefault()  # Evita a busca rápida do navegador
            button_press('÷')
        # Enter para calcular
        elif key == 'Enter':
            equals(ev)
        # Backspace ou Delete para limpar
        elif key in ('Backspace', 'Delete'):
            global equation_text
            equation_text = equation_text[:-1]
            update_display()
        # Escape para limpar tudo
        elif key == 'Escape':
            clear(ev)
    
    document.bind("keydown", handle_keypress)


# Inicializa a calculadora quando o documento estiver pronto
setup_calculator()
