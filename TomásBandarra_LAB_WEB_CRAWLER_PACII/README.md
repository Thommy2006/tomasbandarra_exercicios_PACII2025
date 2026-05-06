# LABORATÓRIO 2

**Descrição**
Laboratório 2 é um **Web Crawler Ético para Fins de Estudo**

**Descrição**

Este projeto tem como objeto criar um Rastreador Web em Python que mapeia a estrutura de ligações de domínios específicos, extrai metadados, identifica relações entre páginas e organiza os dados em ficheiros estruturados, seguindo boas práticas de web scraping e polidez de rede.

**Funcionalidades/Requisitos:**
- Aceder a página inicial
- Extrai título da página e todos links
- Visitar até N páginas
- Evitar visitar a mesma página duas vezes
- Guarda os dados num ficheiro JSON
- NÃO fazer crawling em sites que proibem explicitamente no robots.txt 

**Regras:**
- Ler o ficheiro robots.txt do site 
- Não fazer muitos pedidos seguidos usar o delay 
- o	Identificar com o User-Agent


**Bónus:**
- Filtrar links do mesmo domínio
- Extrair cabeçalhos (h1, h2)
- Extrair parágrafos
- Criar um pequeno gráfico de navegação entre páginas 



**Perguntas de reflexão**
1. Porque é importante respeitar o robots.txt? 
2. O que pode acontecer se um crawler for mal implementado? 
3. Qual a diferença entre crawling e scraping?


# Como usar:
O projeto requer Python 3.x.

**Primeiro instalar bibliotecas**

```bash
pip install requests beautifulsoup4
```

**Depois de instalado a biblioteca executar o comando**

```bash
python crawler.py
```

**Como resultado o programa vai criar um ficherio JSON com os dados extraidos**