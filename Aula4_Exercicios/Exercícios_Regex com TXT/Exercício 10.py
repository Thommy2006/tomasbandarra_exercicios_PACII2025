# Exercício 10: Extrair apenas os domínios dos sites


import re

with open('registos.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    dominios = re.findall(r'Site:\shttps?://(?:www\.)?([A-Za-z0-9.-]+\.[A-Za-z]{2,})', conteudo)
    print("\nDominios:")
    for dominio in dominios:
        print(dominio)