# Exercício 7: Extrair todos os NIFs (9 dígitos)


import re

with open('registos.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    nifs = re.findall(r'NIF:\s(\d{9})', conteudo)
    print("\nNIFs:")
    for nif in nifs:
        print(nif)