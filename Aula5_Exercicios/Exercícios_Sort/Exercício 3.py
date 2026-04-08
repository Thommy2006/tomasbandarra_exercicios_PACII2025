# Exercício 3: Ordenar caracteres de uma palavra


palavra = "algoritmo"
caracteres = list(palavra)

troca = True
while troca:
    troca = False
    for i in range(len(caracteres)-1):
        if caracteres[i] > caracteres[i+1]:
            caracteres[i], caracteres[i+1] = caracteres[i+1], caracteres[i]
            troca = True

resultado = ''.join(caracteres)
print(resultado)