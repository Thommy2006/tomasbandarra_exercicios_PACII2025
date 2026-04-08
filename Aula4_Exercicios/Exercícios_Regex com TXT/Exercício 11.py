# Exercício 11: Validar se todos os NIFs começam com um dígito válido


import re

with open('registos.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    nifs = re.findall(r'NIF:\s(\d{9})', conteudo)
    
    digitos_validos = ['1', '2', '3', '5', '6', '8']
    print("\nValidar NIFs:")
    for nif in nifs:
        letra_digito = nif[0]
        if letra_digito in digitos_validos:
            print(f"{nif} - Digito Valido: {letra_digito}")
        else:
            print(f"{nif} - Digito Invalido: {letra_digito}")