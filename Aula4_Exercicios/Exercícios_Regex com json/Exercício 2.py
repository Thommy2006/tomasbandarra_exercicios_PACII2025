# Exercicio 2 : Validar emails com regex


import json
import re

with open('dados.json', 'r', encoding='utf-8') as ficheiro:
    dados = json.load(ficheiro)


formato_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

print("Validar emails com regex:\n")

for pessoa in dados:
    email = pessoa['email']
    nome = pessoa['nome']
    
    if re.match(formato_email, email):
        print(f"{nome}: {email}")
    else:
        print(f"{nome}: {email}")