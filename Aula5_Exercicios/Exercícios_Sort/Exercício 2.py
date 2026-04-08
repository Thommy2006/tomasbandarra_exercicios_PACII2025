# Exercício 2: Ordenar por ordem inversa (Z → A), ignorando maiúsculas/minúsculas


palavras = ["Python", "inteligencia", "Aprender", "dados", "Rede"]

troca = True
while troca:
    troca = False
    for i in range(len(palavras)-1):
        
        l1 = palavras[i].lower()
        l2 = palavras[i+1].lower()
        
        if l1 < l2:
            palavras[i], palavras[i+1] = palavras[i+1], palavras[i]
            troca = True

print(palavras)