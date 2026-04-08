# Exercício 2: Encontrar todos os emails

with open('dados.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', conteudo)
    print("\nEmails:")
    for Email in emails:
        print(email)