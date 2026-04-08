# Exercício 4: Extrair apenas os nomes


import re

with open('dados.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    nomes = re.findall(r'Nome:\s([^,\n]+)', conteudo)
    print("\nNomes:")
    for nome in nomes:
        print(nome.strip())