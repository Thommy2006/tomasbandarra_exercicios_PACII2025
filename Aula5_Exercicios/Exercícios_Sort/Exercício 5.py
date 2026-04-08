# Exercício 5: Agrupar palavras pela letra inicial e ordenar cada grupo


palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]

grupos = {}
for palavra in palavras:
    letra = palavra[0]
    if letra not in grupos:
        grupos[letra] = []
    grupos[letra].append(palavra)

for letra in grupos:
    troca = True
    while troca:
        troca = False
        for i in range(len(grupos[letra]) - 1):
            if grupos[letra][i] > grupos[letra][i + 1]:
                grupos[letra][i], grupos[letra][i + 1] = grupos[letra][i + 1], grupos[letra][i]
                troca = True

print("\nResultado esperado:")
print(grupos)