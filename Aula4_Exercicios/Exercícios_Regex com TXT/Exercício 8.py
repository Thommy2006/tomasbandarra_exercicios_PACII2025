# Exercício 8: Extrair datas no formato DD/MM/AAAA


import re

with open('registos.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    datas = re.findall(r'Data:\s(\d{2}/\d{2}/\d{4})', conteudo)
    print("\nDatas:")
    for data in datas:
        print(data)