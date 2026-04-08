# Exercício 6: Validar emails que terminam em .pt


import re

with open('dados.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    emails_pt = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.pt\b', conteudo)
    print("\nEmails que acabam com (.pt):\n")
    for email in emails_pt:
        print(email)