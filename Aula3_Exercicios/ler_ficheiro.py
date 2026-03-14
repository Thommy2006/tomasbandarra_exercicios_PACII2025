# Ler o ficheiro

lista1 = []
lista2 = []

try:
    f = open('dados.txt', 'r')
    linhas = f.readlines()
    f.close()
    
    for linha in linhas:
        if ',' in linha:
            nome, morada = linha.strip().split(',', 1)
            lista1.append(nome)
            lista2.append(morada)
            
except:
    print("Ficheiro vazio")

while True:
    print("\n1.Inserir")
    print("2.Listar")
    print("3.Salvar")
    print("4.Sair")
    
    escolha = input("Escolha: ")
    
    if opescolha == "1":
        lista1.append(input("Insert nome: "))
        lista2.append(input("Insert morada: "))
        
    elif escolha == "2":
        for i in range(len(lista1)):
            print(f"Nome: {lista1[i]} \nMorada: {lista2[i]}")
            
    elif escolha == "3":
        f = open('dados.txt', 'w')
        for i in range(len(lista1)):
            f.write(f"{lista1[i]},{lista2[i]}\n")
        f.close()
        print("Guardado!")
        
    elif escolha == "4":
        f = open('dados.txt', 'w')
        for i in range(len(lista1)):
            f.write(f"{lista1[i]},{lista2[i]}\n")
        f.close()
        breaks