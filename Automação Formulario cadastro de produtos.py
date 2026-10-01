




# pyautogui.click -> clica 
# pyautogui.write -> escreve
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)

import pyautogui
import time 
# importar o time para poder usar o time.sleep() e fazer pausas no código
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# esperar 1 segundo entre cada comando
 # passo 1: entrar no sistema da empresa 
# abrir o navegador
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")
pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa de 3 seg para o site carregar
time.sleep(1)
# passo 2: fazer login 
# clicar na aba de email
pyautogui.click(x=767, y=463)
pyautogui.write("soareshenderson78@outlook.com")
pyautogui.press("tab")
pyautogui.write("1234567890")
pyautogui.press("enter")
pyautogui.press("tab")
# fazer uma pausa de 3 seg para o site carregar
time.sleep(1)
# passo 3: abrir a base de dados (importar o arquivo) 
# pip install pandas openpyxl 
import pandas
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    # USAR O TAB  para criar a margem para as linhas que vão se repetir
    # index para puxar os indices da tabela.

# passo 4: cadastrar o 1° produto
#código do produto
    pyautogui.click(x=769, y=338)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #código da marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #código do tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # código da categorian  
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # código do preço unitário
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    # código do custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # código da observação
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs)
    pyautogui.press("tab") # passar pro botão de enviar
    pyautogui.press("enter") # apertar o botão de enviar

    # passo 5: repetir o passo 4 até acabar os produtos
    pyautogui.scroll(5000)