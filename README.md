# Automação de Cadastro de Produtos com Python

Projeto desenvolvido em Python com o objetivo de automatizar o processo de cadastro de produtos em um sistema web.

A automação utiliza o **PyAutoGUI** para controlar teclado e mouse e o **Pandas** para realizar a leitura dos dados de um arquivo CSV.

## Objetivo do projeto

O objetivo foi automatizar uma tarefa repetitiva de cadastro de produtos, evitando o preenchimento manual de cada registro.

O script:

- abre o navegador;
- acessa o sistema;
- realiza o login;
- importa os dados de um arquivo CSV;
- percorre todos os produtos;
- preenche os campos automaticamente;
- envia cada cadastro.

## Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas
- CSV
- Google Chrome

## Como funciona

Primeiro, o script abre o navegador e acessa o sistema utilizando o endereço definido no código.

Depois, o PyAutoGUI realiza interações com a página utilizando comandos como:

```python
pyautogui.click()
pyautogui.write()
pyautogui.press()
pyautogui.hotkey()
