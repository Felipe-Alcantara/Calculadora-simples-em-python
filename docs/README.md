# Calculadora Pro - Versão Brython

Este é um projeto de calculadora desenvolvido em Python com Tkinter, agora também disponível para web usando **Brython** (Python no navegador).

## 🚀 Versão Web (Brython)

A calculadora está disponível para uso direto no navegador! Basta abrir o arquivo `docs/index.html` em qualquer navegador moderno.

### Como executar:

1. **Opção 1 - Abrir diretamente:**
   - Navegue até a pasta `docs`
   - Clique duas vezes no arquivo `index.html`
   - A calculadora abrirá no seu navegador padrão

2. **Opção 2 - Servidor local (recomendado):**
   ```bash
   cd docs
   python -m http.server 8000
   ```
   - Acesse: `http://localhost:8000`

3. **Opção 3 - GitHub Pages:**
   - Faça deploy da pasta `docs` no GitHub Pages
   - A calculadora ficará disponível online

### Recursos da versão web:
- ✨ Design moderno e responsivo
- 🎨 Tema dark com cores vibrantes
- ⌨️ Suporte para teclado:
  - Números e operadores funcionam normalmente
  - `Enter` para calcular
  - `Backspace` para apagar último dígito
  - `Escape` para limpar tudo
- 📱 Totalmente responsiva (funciona em mobile)

## 🖥️ Versão Desktop (Tkinter)

Execute o arquivo Python principal para usar a versão desktop:

```bash
python "Calculadora (Editado e finalizado).py"
```

## 📁 Estrutura do Projeto

```
├── Calculadora (Editado e finalizado).py  # Versão Tkinter
├── docs/
│   ├── index.html        # Página HTML principal
│   ├── style.css         # Estilos da calculadora
│   └── calculator.py     # Lógica em Python (Brython)
├── LICENSE
└── README.md
```

## 🎨 Recursos

- Operações básicas: adição, subtração, multiplicação e divisão
- Interface intuitiva e moderna
- Tratamento de erros (divisão por zero, sintaxe inválida)
- Design consistente entre versão desktop e web

## 👨‍💻 Autor

**By: dj_felixo**

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
