import pyautogui
import time
import pandas as pd

pyautogui.hotkey("ctrl", "t")
pyautogui.write("link-do-diretorio-onde-esta-o-banco-de-dados")
pyautogui.press("Enter")
time.sleep(2)

pyautogui.click(x=879, y=579)
pyautogui.write("meu_login")

pyautogui.click(x=832, y=679)
pyautogui.write("minha_senha")

pyautogui.click(x=900, y=787)
time.sleep(2)

pyautogui.click(x=373, y=439)
pyautogui.click(x=837, y=268)
pyautogui.click(x=956, y=720)
time.sleep(2)
pyautogui.press("Enter")
time.sleep(10)

Tabela = pd.read_csv(r"caminho-ate-o-arquivo-baixado", sep=";")

total_gasto = Tabela["ValorFinal"].sum()
quantidade = Tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=169, y=314)
time.sleep(1)

#preenchendo o e-mail
pyautogui.write("seu-email")
pyautogui.press("enter")
pyautogui.press("Tab")

assunto_do_email = "Relatório diário de compra"
pyperclip.copy(assunto_do_email)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("Tab")
time.sleep(1)

texto = f"""
Prezados,
Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida, é só falar.
Att., Pedro
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
