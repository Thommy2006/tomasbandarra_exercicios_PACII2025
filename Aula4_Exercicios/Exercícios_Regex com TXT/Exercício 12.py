# Exercício 12: Criar um ficheiro resumo.txt com os dados organizados


import re

with open('registos.txt', 'r', encoding='utf-8') as f:
    linhas = f.readlines()

with open('resumo.txt', 'w', encoding='utf-8') as f_out:
    for linha in linhas:
        nome = re.search(r'Nome:\s([^|]+)', linha)
        nif = re.search(r'NIF:\s(\d{9})', linha)
        data = re.search(r'Data:\s(\d{2}/\d{2}/\d{4})', linha)
        codigo = re.search(r'Código Postal:\s(\d{4}-\d{3})', linha)
        site = re.search(r'Site:\shttps?://(?:www\.)?([A-Za-z0-9.-]+\.[A-Za-z]{2,})', linha)
        
        if nome and nif and data and codigo and site:
            f_out.write(f"{nome.group(1).strip()} | {nif.group(1)} | {data.group(1)} | {codigo.group(1)} | {site.group(1)}\n")

print("\nFicheiro resumo.txt criado.")