# Automatização de relatório

Objetivo do projeto: o projeto consiste em automatizar o envio de e-mails diários contendo o gasto total na compra de produtos, a quantidade de produtos e o valor médio, em formato de relatorio

```
!pip install pyautogui
!pip install pyperclip
!pip install pandas

import pyautogui
import pyper clip
import time
import pandas as pd
```

é necessário instalar as bibliotecas mostradas para que o script rode.

Projeto feito em jupyter notebook

Inicialmente, é necessário automatizar a entrada no sistema para baixar banco de dados; 

Posteriormente, é feito o download do arquivo com os dados;

Após baixar o banco de dados, fazer tratativas usando o pandas

Automatizar a entrada na plataforma de e-mail escolhido e completar os dados do e-mail.
