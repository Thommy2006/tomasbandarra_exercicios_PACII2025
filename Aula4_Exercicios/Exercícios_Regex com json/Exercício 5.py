# Exercicio 5 : Guardar apenas os registos válidos num novo ficheiro JSON


import json
import re

with open('dados.json', 'r', encoding='utf-8') as ficheiro:
    dados = json.load(ficheiro)

formato_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
formato_nif = r'^[123568]\d{8}$'

validos = []

print("Validar registos:\n")

for pessoa in dados:
    nome = pessoa['nome']
    email = pessoa['email']
    nif = pessoa['nif']
    telemovel = pessoa['telemovel']
    
    if re.match(formato_email, email):
        email_valido = True
    else:
        email_valido = False
    
    if re.match(formato_nif, nif):
        nif_valido = True
    else:
        nif_valido = False
    
    numero = re.sub(r'\D', '', telemovel)
    if len(numero) == 9:
        telemovel_valido = True
    else:
        telemovel_valido = False
    
    
    if email_valido and nif_valido and telemovel_valido:
        validos.append(pessoa)
        print(f"{nome}: Guardado e valido")
    else:
        print(f"{nome}: Nao foi guardado e nao e valido  ")

with open('Dados_validados.json', 'w', encoding='utf-8') as ficheiro:
    json.dump(validos, ficheiro, indent=2, ensure_ascii=False)