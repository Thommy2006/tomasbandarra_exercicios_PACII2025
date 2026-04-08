# Exercício 3: Encontrar todos os números de telemóvel


import re

with open('dados.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    

    Telemóvel = re.findall(r'\b\d{9}\b|\b\d{3}-\d{3}-\d{3}\b|\b\d{3}\s\d{3}\s\d{3}\b', conteudo)
    print("\nNumeros de telemóvel:")
    for Telemóvel in Telemóvel:
        print(Telemóvel)