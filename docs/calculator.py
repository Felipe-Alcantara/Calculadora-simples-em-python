"""
Calculadora Científica Pro - Versão Brython
By: dj_felixo
"""

from browser import document, html  # type: ignore
from datetime import datetime
import math

# Variável global para armazenar a equação
equation_text = ""

# Lista para armazenar o histórico
history = []


def scientific_operation(operation):
    """Executa operações científicas"""
    global equation_text
    try:
        if equation_text:
            # Substitui símbolos para cálculo
            calc_text = equation_text.replace('×', '*').replace('÷', '/')
            current_value = float(eval(calc_text))
            original = equation_text
            
            if operation == 'sqrt':
                result = math.sqrt(current_value)
                calc_display = f"√({original})"
            elif operation == 'square':
                result = current_value ** 2
                calc_display = f"({original})²"
            elif operation == 'power':
                equation_text = equation_text + "**"
                update_display()
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
            update_display()
    except ValueError:
        document["display"].text = "Erro: Valor inválido"
        equation_text = ""
    except ZeroDivisionError:
        document["display"].text = "Erro: Divisão por 0"
        equation_text = ""
    except Exception:
        document["display"].text = "Erro"
        equation_text = ""


def insert_constant(constant):
    """Insere constantes matemáticas"""
    global equation_text
    if constant == 'pi':
        equation_text = equation_text + str(math.pi)
    elif constant == 'e':
        equation_text = equation_text + str(math.e)
    update_display()


def backspace(ev=None):
    """Remove o último caractere"""
    global equation_text
    equation_text = equation_text[:-1]
    update_display()


def add_to_history(calculation, result):
    """Adiciona um cálculo ao histórico"""
    now = datetime.now()
    timestamp = now.strftime("%H:%M:%S")
    
    # Adiciona ao histórico
    history.append({
        'time': timestamp,
        'calculation': calculation,
        'result': result
    })
    
    # Atualiza a exibição
    update_history_display()


def update_history_display():
    """Atualiza a exibição do histórico"""
    history_list = document["history-list"]
    history_list.clear()
    
    if not history:
        empty_msg = html.P("Nenhum cálculo ainda...", Class="history-empty")
        history_list <= empty_msg
    else:
        # Mostra os cálculos mais recentes primeiro
        for calc in reversed(history):
            item = html.DIV(Class="history-item")
            
            time_elem = html.DIV(calc['time'], Class="history-time")
            calc_elem = html.DIV(f"{calc['calculation']} =", Class="history-calculation")
            result_elem = html.DIV(calc['result'], Class="history-result")
            
            item <= time_elem
            item <= calc_elem
            item <= result_elem
            
            history_list <= item


def clear_history(ev):
    """Limpa todo o histórico"""
    global history
    history = []
    update_history_display()


def button_press(num):
    """Adiciona um número ou operador ao display"""
    global equation_text
    equation_text = equation_text + str(num)
    update_display()


def equals(ev):
    """Calcula o resultado da equação"""
    global equation_text
    try:
        if equation_text:
            # Salva a expressão original
            original_expression = equation_text
            
            # Substitui os símbolos visuais pelos operadores Python
            calc_text = equation_text.replace('×', '*').replace('÷', '/')
            total = str(eval(calc_text))
            
            # Adiciona ao histórico
            add_to_history(original_expression, total)
            
            # Atualiza o display
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
    document["btn-clear-history"].bind("click", clear_history)
    
    # Botões científicos - operações
    document["btn-sqrt"].bind("click", lambda ev: scientific_operation('sqrt'))
    document["btn-square"].bind("click", lambda ev: scientific_operation('square'))
    document["btn-power"].bind("click", lambda ev: scientific_operation('power'))
    document["btn-percent"].bind("click", lambda ev: scientific_operation('percent'))
    document["btn-inverse"].bind("click", lambda ev: scientific_operation('inverse'))
    
    # Botões científicos - trigonometria e logaritmos
    document["btn-sin"].bind("click", lambda ev: scientific_operation('sin'))
    document["btn-cos"].bind("click", lambda ev: scientific_operation('cos'))
    document["btn-tan"].bind("click", lambda ev: scientific_operation('tan'))
    document["btn-log"].bind("click", lambda ev: scientific_operation('log'))
    document["btn-ln"].bind("click", lambda ev: scientific_operation('ln'))
    
    # Constantes e extras
    document["btn-pi"].bind("click", lambda ev: insert_constant('pi'))
    document["btn-e"].bind("click", lambda ev: insert_constant('e'))
    document["btn-lparen"].bind("click", lambda ev: button_press('('))
    document["btn-rparen"].bind("click", lambda ev: button_press(')'))
    document["btn-backspace"].bind("click", backspace)
    
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
        # Backspace ou Delete para apagar
        elif key in ('Backspace', 'Delete'):
            backspace()
        # Escape para limpar tudo
        elif key == 'Escape':
            clear(ev)
    
    document.bind("keydown", handle_keypress)


# Inicializa a calculadora quando o documento estiver pronto
setup_calculator()
update_history_display()
