# Exercicio 3 : Extrair domínios dos sites


import json
import re


with open('dados.json', 'r', encoding='utf-8') as ficheiro:
    dados = json.load(ficheiro)

sites = r'https?://(?:www\.)?([^/]+)'

print("Extrair dominios:\n")


for pessoa in dados:
    site = pessoa['site']
    nome = pessoa['nome']
    
    resultado = re.search(sites, site)
    if resultado:
        print(f"{nome}: {site}")