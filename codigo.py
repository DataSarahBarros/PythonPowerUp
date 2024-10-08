# Passo 1: Entrar no sistema da e empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui (biblioteca)
import pyautogui

# comandos do pyautogui:
# pyautogui.write -> escrever texto
# pyautogui.click -> clicar com o mause
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar um atalho de teclado (Ctrl, C) Exemplo: pyautogui.hotkey ("command", "entender") or ("ctrl", "c")
# pyautogui.MAUSE = 0.5 seconds or 1 seconds = serve para dar tempo entre uma etapa e outro
# para dar pause em um lugar especifico é preciso chamar a biblioteca "time" = import time (não precisa instalar)

# comandos diferentes para funções diferentes:

import time

pyautogui.PAUSE = 1

# abrir o navegador
# apertar tecla in
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")




# Passo 2: Fazer login
# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# variavel link recbe um valor 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# sempre que precisar do valor, chame a variavel
pyautogui.write(link)
pyautogui.press("enter")
 
# Dar uma pausa de 3 seconds:
time.sleep(1)
# Bot de automação RPA = robot processing automation
pyautogui.click(x=656, y=496)
pyautogui.write("202307631957@alunos.estacio.br")
# passar para o proximo campo
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=964, y=693)

time.sleep(2)





# Passo 3: Importar a base de dados
# PANDAS é um pacote de codigo do python que serve para trabalhar com base de dados
# pip install pandas
import pandas

# read = ler, ler um arquivo
# a variavel (tabela) recebe o valor "produto.csv"
# colocar o arquivo na mesma pasta onde o VScode esta logado
tabela = pandas.read_csv("produtos.csv")
print(tabela)




# Passo 4: Cadastrar 1 produto
pyautogui.click(x=632, y=348)

# localizar um item em uma tabela, atribuir a variavel tabela = tabela.loc (colalizar)
# lista de informações no pandas se usou [colchete] = [linha, coluna]
# variavel = tabela.loc[linha, coluna]

linha = 0

# texto = string = stc() = no python tranformar em texto

# codigo
codigo = tabela.loc[linha, "codigo"]
pyautogui.write(str(codigo))
pyautogui.press("tab")
# marca
marca = tabela.loc[linha, "marca"]
pyautogui.write(str(marca))
pyautogui.press("tab")
# tipo
tipo = tabela.loc[linha, "tipo"]
pyautogui.write(str(tipo))
pyautogui.press("tab")
# categoria
categoria = tabela.loc[linha, "categoria"]
pyautogui.write(str(categoria))
pyautogui.press("tab")
# preco unitario
preco = tabela.loc[linha, "preco unitario"]
pyautogui.write(str(preco))
pyautogui.press("tab")
# custo
custo = tabela.loc[linha, "custo"]
pyautogui.write(str(custo))
pyautogui.press("tab")
# obs
obs = tabela.loc[linha, "obs"]
pyautogui.write(str(obs))
pyautogui.press("tab")
# clicar no botão enviar
pyautogui.press("enter")
















# Passo 5: Redefinir o processo de cadastro até acabar os produtos


