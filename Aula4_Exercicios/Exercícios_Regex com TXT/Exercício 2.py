# Exercício 2: Encontrar todos os emails


import re

with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', conteudo)

for email in emails:
    print(email)