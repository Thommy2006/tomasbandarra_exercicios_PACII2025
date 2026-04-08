# Exercício 5: Guardar os dados extraídos num novo ficheiro


import re

with open('dados.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()

nomes = re.findall(r'Nome:\s(.+)', conteudo)
emails = re.findall(r'Email:\s(.+)', conteudo)
telefones = re.findall(r'Telemóvel:\s(.+)', conteudo)

with open('extraidos.txt', 'w', encoding='utf-8') as f_out:
    for i in range(len(nomes)):
        f_out.write(f"{nomes[i]} | {emails[i]} | {telefones[i]}\n")

print("Ficheiro extraidos.txt criado.")