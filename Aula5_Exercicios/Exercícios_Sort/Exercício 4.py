# Exercício 4: Ordenar lista de palavras pela quantidade de letras minúsculas


palavras = ["PYthon", "banana", "CODIGO", "intELIGENTE", "dados"]

def contar_minusculas(p):
    conta = 0
    for letra in p:
        if 'a' <= letra <= 'z':
            conta += 1
    return conta

troca = True
while troca:
    troca = False
    for i in range(len(palavras) - 1):
        if contar_minusculas(palavras[i]) > contar_minusculas(palavras[i + 1]):
            palavras[i], palavras[i + 1] = palavras[i + 1], palavras[i]
            troca = True

print(palavras)