# Exercício 1: Ler o ficheiro


with open('dados.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    print("Conteudo do ficheiro:")
    print(conteudo)