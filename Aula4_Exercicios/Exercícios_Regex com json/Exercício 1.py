# Exercicio 1 : Ler o ficheiro JSON


import json

with open('dados.json', 'r', encoding='utf-8') as ficheiro:
    dados = json.load(ficheiro)

print("Dados do ficheiro:")
for pessoa in dados:
    print(pessoa)