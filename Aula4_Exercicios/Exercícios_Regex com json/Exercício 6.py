# Exercicio 6 : Criar um ficheiro .txt  com a keys nome e email


import json

with open('dados.json', 'r', encoding='utf-8') as ficheiro:
    dados = json.load(ficheiro)

with open('Novo.txt', 'w', encoding='utf-8') as txt:
    for pessoa in dados:
        nome = pessoa['nome']
        email = pessoa['email']
        txt.write(f"Nome: {nome}\n")
        txt.write(f"Email: {email}\n")
        txt.write("\n\n")

print("Foi criado o ficheiro 'Novo.txt'.")