# Exercício 13: Encontrar registos com datas anteriores a 2025


import re
from datetime import datetime

with open('registos.txt', 'r', encoding='utf-8') as f:
    
    print("\nRegistos com datas anteriores a 2025:\n")
    
    for linha in f:
        match = re.search(r'Data:\s(\d{2})/(\d{2})/(\d{4})', linha)
        if match:
            data = datetime(int(match.group(3)), int(match.group(2)), int(match.group(1)))
            if data.year < 2025:
                nome = re.search(r'Nome:\s([^|]+)', linha)
                print(f"{nome.group(1).strip()} - {match.group(0)}")