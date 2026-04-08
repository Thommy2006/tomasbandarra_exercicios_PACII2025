# Exercício 1: Ordenar palavras por ordem alfabética (A → Z)


palavras = ["banana", "uva", "abacaxi", "laranja"]

troca = True
while troca:
    troca = False
    for i in range(len(palavras)-1):
        if palavras[i] > palavras[i+1]:
            palavras[i], palavras[i+1] = palavras[i+1], palavras[i]
            troca = True

print(palavras)