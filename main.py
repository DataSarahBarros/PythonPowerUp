import pyautogui
import time

pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=642, y=486)
pyautogui.write("sarahbarros.bi@gmail.com")

pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=979, y=694)

time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)
    
for linha in tabela.index:
    pyautogui.click(x=631, y=390)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    custo = tabela.loc[linha, "obs"]
    pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)

    time.sleep(1)