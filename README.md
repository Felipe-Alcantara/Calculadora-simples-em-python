<div align="center">

# 🧮 Calculadora Pro

### Uma calculadora moderna e elegante desenvolvida em Python

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![Brython](https://img.shields.io/badge/Web-Brython-orange.svg)](https://brython.info/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Demo-Online-success.svg)](https://felipe-alcantara.github.io/Calculadora-simples-em-python/)

[🌐 Demo Online](https://felipe-alcantara.github.io/Calculadora-simples-em-python/) • [🚀 Instalação](#-instalação) • [💻 Uso](#-uso) • [🌟 Features](#-features)

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="80" height="80"/>

---

</div>

## 📖 Sobre o Projeto

Este projeto é uma calculadora completa desenvolvida em Python, disponível em **duas versões**:

- **🖥️ Desktop**: Interface gráfica usando Tkinter com design moderno
- **🌐 Web**: Versão Brython que roda diretamente no navegador

O projeto começou como um exercício de aprendizado e evoluiu para uma aplicação com interface profissional, demonstrando conceitos de GUI, tratamento de eventos e design responsivo.

---

## ✨ Features

### 🎨 Interface Moderna
- ✅ Design dark mode elegante com gradientes
- ✅ Cores vibrantes e intuitivas para diferentes tipos de botões
- ✅ Display de alta legibilidade com fonte personalizada
- ✅ Efeitos visuais e animações suaves

### 🔧 Funcionalidades
- ➕ Operações básicas: adição, subtração, multiplicação e divisão
- 🔢 Suporte para números decimais
- 🧹 Botão de limpeza (Clear)
- ⚠️ Tratamento de erros (divisão por zero, sintaxe inválida)
- ⌨️ Suporte completo para teclado (versão web)

### 📱 Responsividade
- 📐 Layout adaptativo para diferentes tamanhos de tela
- 🖱️ Botões com feedback visual ao clicar
- 💡 Interface intuitiva e fácil de usar

---

## 🚀 Instalação

### Versão Desktop (Tkinter)

#### Pré-requisitos
- Python 3.8 ou superior
- Tkinter (geralmente já vem com Python)

#### Instalação

```bash
# Clone o repositório
git clone https://github.com/Felipe-Alcantara/Calculadora-simples-em-python.git

# Entre na pasta do projeto
cd Calculadora-simples-em-python

# Execute a calculadora
python "Calculadora (Editado e finalizado).py"
```

### Versão Web (Brython)

#### Opção 1: Abrir diretamente no navegador

```bash
# Navegue até a pasta docs
cd docs

# Abra o arquivo index.html no navegador
# Windows:
start index.html

# Linux/Mac:
open index.html
```

#### Opção 2: Servidor local (Recomendado)

```bash
# Entre na pasta docs
cd docs

# Inicie um servidor HTTP simples
python -m http.server 8000

# Acesse no navegador
# http://localhost:8000
```

---

## 💻 Uso

### Versão Desktop

1. Execute o arquivo Python:
   ```bash
   python "Calculadora (Editado e finalizado).py"
   ```

2. Use o mouse para clicar nos botões ou digite diretamente

3. Operações disponíveis:
   - **Números**: 0-9
   - **Operadores**: +, -, ×, ÷
   - **Decimal**: .
   - **Limpar**: C
   - **Calcular**: =

### Versão Web

1. Acesse a calculadora no navegador

2. **Atalhos de teclado**:
   - `0-9`: Números
   - `+`, `-`, `*`, `/`: Operadores
   - `Enter`: Calcular resultado
   - `Backspace`: Apagar último dígito
   - `Escape`: Limpar tudo

---

## 📁 Estrutura do Projeto

```
Calculadora-simples-em-python/
├── 📄 Calculadora (Editado e finalizado).py  # Versão Desktop (Tkinter)
├── 📁 docs/                                   # Versão Web (Brython)
│   ├── 📄 index.html                         # Página principal
│   ├── 🎨 style.css                          # Estilos e design
│   ├── 🐍 calculator.py                      # Lógica em Python
│   └── 📝 README.md                          # Documentação web
├── 📜 LICENSE                                 # Licença MIT
└── 📖 README.md                               # Este arquivo
```

---

## 🎨 Paleta de Cores

A calculadora utiliza um esquema de cores cuidadosamente selecionado:

| Elemento | Cor | Código |
|----------|-----|--------|
| Background Principal | Cinza Escuro | `#1e1e2e` |
| Display | Cinza Médio | `#2e2e3e` |
| Texto Display | Verde Neon | `#00ff88` |
| Botões Numéricos | Roxo Escuro | `#3e3e5e` |
| Botões Operadores | Laranja | `#ff6b35` |
| Botão Clear | Roxo Claro | `#6b5eff` |
| Botão Igual | Verde Vibrante | `#00ff88` |

---

## 🌐 Demo Online

Você pode testar a versão web da calculadora diretamente no GitHub Pages:

👉 **[https://felipe-alcantara.github.io/Calculadora-simples-em-python/](https://felipe-alcantara.github.io/Calculadora-simples-em-python/)**

🎮 **Experimente agora mesmo sem instalar nada!**

---

## 🛠️ Tecnologias Utilizadas

### Desktop
- **Python 3.x**: Linguagem de programação
- **Tkinter**: Framework para interface gráfica
- **Font**: Módulo para fontes personalizadas

### Web
- **HTML5**: Estrutura da página
- **CSS3**: Estilização e responsividade
- **Brython 3.12**: Python no navegador
- **JavaScript**: Carregamento do Brython

---

## 🎯 Aprendizados

Este projeto demonstra:

- ✅ Criação de interfaces gráficas com Tkinter
- ✅ Manipulação de eventos e callbacks
- ✅ Tratamento de exceções em Python
- ✅ Design de UI/UX moderno
- ✅ Conversão de aplicações desktop para web
- ✅ Uso do Brython para executar Python no navegador
- ✅ CSS Grid e Flexbox para layouts responsivos
- ✅ Boas práticas de organização de código

---

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Se você tem alguma sugestão para melhorar este projeto:

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📝 Ideias para Melhorias Futuras

- [ ] Adicionar histórico de cálculos
- [ ] Implementar operações científicas (raiz, potência, etc)
- [ ] Adicionar temas de cores personalizáveis
- [ ] Salvar configurações do usuário
- [ ] Adicionar animações mais elaboradas
- [ ] Implementar conversor de unidades
- [ ] Adicionar modo de cálculo de porcentagem
- [ ] Criar versão mobile nativa (Kivy)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

<div align="center">

**Desenvolvido por dj_felixo**

Projeto criado durante meus estudos de Python, com ajuda de um amigo que me ensinou os fundamentos. 💙

[![GitHub](https://img.shields.io/badge/GitHub-Felipe--Alcantara-black?style=flat&logo=github)](https://github.com/Felipe-Alcantara)

---

### ⭐ Se este projeto foi útil para você, considere dar uma estrela!

**Made with 💚 and Python**

</div>