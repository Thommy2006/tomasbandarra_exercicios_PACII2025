import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import json
from collections import deque

def ler_robots_txt(url_base, user_agent="MeuCrawlerEstudo"):
    """
    Verifica se o robots.txt permite o crawling
    """
    robots_url = urljoin(url_base, "/robots.txt")
    try:
        response = requests.get(robots_url, timeout=5)
        if response.status_code == 200:
            linhas = response.text.split('\n')
            permitido = True
            
            for linha in linhas:
                if linha.lower().startswith('user-agent:'):
                    agente = linha.split(':', 1)[1].strip().lower()
                    if agente == '*' or agente == user_agent.lower():
                        # Verifica se há Disallow para tudo
                        for proxima in linhas[linhas.index(linha)+1:]:
                            if proxima.lower().startswith('user-agent:'):
                                break
                            if proxima.lower().startswith('disallow: /'):
                                print(f"robots.txt proíbe crawling para {user_agent}")
                                return False
        return True
    except:
        
        print("Não foi possível ler robots.txt")
        return True

def extrair_links(url, soup, mesmo_dominio=False, dominio_base=None):
    """
    Extrai todos os links de uma página
    """
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        url_completa = urljoin(url, href)
        
        # Remove âncoras
        url_completa = url_completa.split('#')[0]
        
        # Filtra links inválidos
        if url_completa and url_completa.startswith('http'):
            if mesmo_dominio and dominio_base:
                if urlparse(url_completa).netloc == dominio_base:
                    links.append(url_completa)
            else:
                links.append(url_completa)
    
    return list(set(links))

def extrair_info_pagina(url, soup):
    """
    Extrai informações da página
    """
    
    titulo = soup.find('title')
    titulo_texto = titulo.get_text().strip() if titulo else "Sem título"
    
    cabecalhos = {
        'h1': [h.get_text().strip() for h in soup.find_all('h1')],
        'h2': [h.get_text().strip() for h in soup.find_all('h2')]
    }
    
    paragrafos = [p.get_text().strip() for p in soup.find_all('p') if p.get_text().strip()]
    
    return {
        'url': url,
        'titulo': titulo_texto,
        'links': [],
        'cabecalhos': cabecalhos,
        'paragrafos': paragrafos[:5]
    }

def crawler(url_inicial, max_paginas, delay=1, mesmo_dominio=True):
    """
    Crawler ético que respeita robots.txt e faz delay entre requisições
    """
    

    headers = {
        'User-Agent': 'MeuCrawlerEstudo/1.0 (Aprendizagem - Contato: estudante@exemplo.com)'
    }
    
    dominio_base = urlparse(url_inicial).netloc
    

    if not ler_robots_txt(url_inicial):
        print("Crawling não permitido pelo robots.txt")
        return []
    

    visitadas = set()
    fila = deque([url_inicial])
    resultados = []
    

    paginas_visitadas = 0
    
    print(f"Iniciando crawler em: {url_inicial}")
    print(f"Máximo de páginas: {max_paginas}")
    
    while fila and paginas_visitadas < max_paginas:
        url_atual = fila.popleft()
        

        if url_atual in visitadas:
            continue
        
        print(f"\nVisitando ({paginas_visitadas + 1}/{max_paginas}): {url_atual}")
        
        try:

            response = requests.get(url_atual, headers=headers, timeout=10)
            response.raise_for_status()
            

            if 'text/html' not in response.headers.get('Content-Type', ''):
                print(f"  Ignorando: não é HTML ({response.headers.get('Content-Type')})")
                visitadas.add(url_atual)
                continue
            

            soup = BeautifulSoup(response.text, 'html.parser')
            

            info_pagina = extrair_info_pagina(url_atual, soup)
            

            links_encontrados = extrair_links(url_atual, soup, mesmo_dominio, dominio_base)
            info_pagina['links'] = links_encontrados
            

            resultados.append(info_pagina)
            

            visitadas.add(url_atual)
            paginas_visitadas += 1
            

            novos_links = 0
            for link in links_encontrados:
                if link not in visitadas and link not in fila:
                    fila.append(link)
                    novos_links += 1
            
            print(f"Título: {info_pagina['titulo'][:50]}...")
            print(f"Links encontrados: {len(links_encontrados)}")
            print(f"Novos links adicionados à fila: {novos_links}")
            print(f"Total na fila: {len(fila)}")
            

            time.sleep(delay)
            
        except requests.exceptions.RequestException as e:
            print(f" Erro {url_atual}: {e}")
            visitadas.add(url_atual)
        except Exception as e:
            print(f" Erro: {e}")
            visitadas.add(url_atual)
    
    print(f"\n\nCrawling concluído!")
    print(f"Páginas visitadas: {paginas_visitadas}")
    print(f"Total de páginas na fila não visitadas: {len(fila)}")
    
    return resultados

def guardar_json(dados, nome_ficheiro="output.json"):
    """
    Guarda os resultados em ficheiro JSON
    """
    with open(nome_ficheiro, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print(f"\nDados guardados em {nome_ficheiro}")

def main():
    """
    Função principal para executar o crawler
    """

    url_inicial = "https://example.com"
    max_paginas = 5
    
    print("=" * 60)
    print("WEB CRAWLER ÉTICO PARA ESTUDO")
    print("=" * 60)
    
    # Executa o crawler
    resultados = crawler(url_inicial, max_paginas, delay=1, mesmo_dominio=True)
    
    # Guarda resultados
    if resultados:
        guardar_json(resultados)
        
        # Mostra resumo
        print("\n" + "=" * 60)
        print("RESUMO DOS RESULTADOS")
        print("=" * 60)
        for resultado in resultados:
            print(f"\nURL: {resultado['url']}")
            print(f"Título: {resultado['titulo']}")
            print(f"Links: {len(resultado['links'])} links encontrados")
    else:
        print("Nenhum resultado obtido.")

if __name__ == "__main__":
    main()