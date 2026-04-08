# Exercicio 4 : Validar NIFs com regex


import json
import re

with open('dados.json', 'r', encoding='utf-8') as ficheiro:
    dados = json.load(ficheiro)

formato_nif = r'^[123568]\d{8}$'

print("Validar NIFs:\n")

for pessoa in dados:
    nif = pessoa['nif']
    nome = pessoa['nome']
    
    if re.match(formato_nif, nif):
        print(f"{nome}: {nif}")
    else:
        print(f"{nome}: {nif}")