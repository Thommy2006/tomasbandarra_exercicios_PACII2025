# Exercício 9: Extrair códigos postais portugueses (1234-567)

import re

with open('registos.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    codigos_postais = re.findall(r'Código Postal:\s(\d{4}-\d{3})', conteudo)
    print("\nCodigos postais:")
    for codigo in codigos_postais:
        print(codigo)