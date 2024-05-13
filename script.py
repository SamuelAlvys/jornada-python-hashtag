#  Passo a passo do projeto 

# 1.Abrir o sistema da empresa
import pyautogui

import time

pyautogui.PAUSE = 0.5

#pyautogui.click
#pyautogui.write
#pyautogui.press
#pyautogui.hotkey
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o navegador

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# Acessar o site do sistema  
time.sleep(0.8) 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# 2.Fazer login
time.sleep(1)
pyautogui.click(x=684, y=528)
pyautogui.write("py.teste@gmail.com")
pyautogui.press("enter")

pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

# 3.Abrir/importar a base de dados de proodutos para importar 
#pip install pandas numpy openpyxl
import pandas as pd
tabela = pd.read_csv("produtos.csv")
print(tabela)

# 4.Cadastrar um produto
# 5.Repetir isso até acabar a lista de produtos 
for linha in tabela.index:
    pyautogui.click(x=704, y=369)
    #Código
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
    #Marca
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    #Tipo
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    #Categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    #Preço
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    #Custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
    #Obs
    obs = str(tabela.loc[linha,"obs"])
    if obs == "nan":
        pyautogui.write("")
    else:
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

 