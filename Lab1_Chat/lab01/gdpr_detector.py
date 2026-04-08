import re
import json
import os
from datetime import datetime

# ── Padrões GDPR ──────────────────────────────────────────────────────────────
_EMAIL_RE       = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
_PHONE_RE       = re.compile(r'(\+351|00351)?\s?(9[1236]\d{7}|2\d{8}|\d{3}[\s\-]\d{3}[\s\-]\d{3})')
_IP_RE          = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
_DATE_RE        = re.compile(r'\b(0?[1-9]|[12]\d|3[01])[-/](0?[1-9]|1[0-2])[-/](\d{4}|\d{2})\b')
_CARD_RE        = re.compile(r'\b(?:\d{4}[\s\-]?){3}\d{4}\b')

# Nome próprio: letra MAIÚSCULA inicial + pelo menos 2 letras minúsculas
# NÃO usa IGNORECASE — só apanha palavras genuinamente capitalizadas
_WORD_CAP = r'[A-ZÁÉÍÓÚÀÂÃÊÔÕÇ][a-záéíóúàâãêôõç]{2,}'
_NAME_RE = re.compile(
    r'\b(' + _WORD_CAP + r'(?:\s+(?:de|da|do|dos|das)\s+)?\s+' + _WORD_CAP +
    r'(?:\s+' + _WORD_CAP + r'){0,2})\b'
)

# Stop-words: palavras capitalizadas que NÃO são nomes
_STOP = {
    "Bom","Boa","Olá","Sim","Não","Ok","Ola",
    "Com","Para","Pelo","Pela","Pelos","Pelas","Como","Este","Esta","Esse",
    "Essa","Aquele","Aquela","Isso","Aqui","Mais","Muito","Quando","Desde",
    "Onde","Qual","Quem","Cada","Todo","Toda","Todos","Todas",
    "Fala","Falo","Tens","Tenho","Nasci","Podes","Envia","Fica","Liga",
    "Preciso","Urgente","Clique","Acesse","Ganhou","Parabens","Parabéns",
    "Porta","Servidor","Cartão","Email","Numero","Número","Data","Conta",
    "Senha","Iban","Nib","Mbway","Internet","Sistema","Python","Windows",
    "Obrigado","Obrigada","Até","Tchau","Xau",
}

def _is_valid_name(name: str) -> bool:
    words = [w for w in re.split(r'\s+', name) if w.lower() not in {'de','da','do','dos','das'}]
    if len(words) < 2:
        return False
    for w in words:
        if w in _STOP:
            return False
        if not re.match(r'^[A-ZÁÉÍÓÚÀÂÃÊÔÕÇ][a-záéíóúàâãêôõç]{2,}$', w):
            return False
    return True


def detect_personal_data(message: str) -> dict:
    detected = {}

    if m := _EMAIL_RE.findall(message):
        detected["email"] = m

    phones = [g[1].strip() for g in _PHONE_RE.findall(message) if g[1].strip()]
    if phones:
        detected["phone"] = phones

    if m := _IP_RE.findall(message):
        detected["ip_address"] = m

    if m := _DATE_RE.findall(message):
        detected["birth_date"] = ["/".join(g) for g in m]

    if m := _CARD_RE.findall(message):
        detected["credit_card"] = m

    names = [n for n in _NAME_RE.findall(message) if _is_valid_name(n)]
    if names:
        detected["full_name"] = names

    return detected


def detect_social_engineering(message: str) -> list:
    SOCIAL_PATTERNS = [
        r"\b(password|palavra.?passe|senha|pin)\b",
        r"\b(conta banc[aá]ria|iban|nib|mbway)\b",
        r"\b(urgente|transfer[eê]ncia|transferir dinheiro)\b",
        r"\b(clique aqui|click here|acesse o link)\b",
        r"\b(ganhou|pr[eé]mio|oferta especial|parab[eé]ns)\b",
    ]
    return [p for p in SOCIAL_PATTERNS if re.search(p, message, re.IGNORECASE)]


def _load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def _save_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_personal_data(username: str, message: str, detected: dict,
                       filepath: str = "personal_data_log.json"):
    logs = _load_json(filepath)
    logs.append({"timestamp": datetime.now().isoformat(),
                 "username": username, "message": message, "detected": detected})
    _save_json(filepath, logs)


def save_social_engineering(username: str, message: str, patterns: list,
                            filepath: str = "social_engineering_log.json"):
    logs = _load_json(filepath)
    logs.append({"timestamp": datetime.now().isoformat(),
                 "username": username, "message": message, "patterns": patterns})
    _save_json(filepath, logs)


# ── Demo / Teste rápido ───────────────────────────────────────────────────────
if __name__ == "__main__":
    test_messages = [
        ("EMAIL",       "Olá, o meu email é joao.bravo@gmail.com, podes contactar-me!"),
        ("TELEFONE",    "O meu número é 912345678, liga-me quando puderes."),
        ("IP",          "O servidor está em 192.168.1.100, porta 8080."),
        ("DATA NASC.",  "Nasci em 15/03/1998, tenho 27 anos."),
        ("CARTÃO",      "Cartão: 1234 5678 9012 3456 — paga com isto."),
        ("NOME",        "Fala com João Bravo Silva sobre o assunto."),
        ("NOME",        "Envia para Maria João Ferreira por favor."),
        ("SOC. ENG.",   "URGENTE: preciso que me envies a tua senha e o IBAN!"),
        ("LIMPA",       "Bom dia a todos, como estão?"),
        ("LIMPA",       "Qual é o horário de funcionamento?"),
    ]

    print("=" * 65)
    print("  GDPR Detector — Teste de Mensagens")
    print("=" * 65)

    for label, msg in test_messages:
        detected = detect_personal_data(msg)
        social   = detect_social_engineering(msg)
        status   = "LIMPA   " if not detected and not social else "BLOQUEADA"
        print(f"\n[{label:<10}] {msg}")
        print(f"  Estado : {status}")
        for dtype, vals in detected.items():
            print(f"  ⚠ GDPR [{dtype}]: {vals}")
        if social:
            print(f"  ⚠ ENG. SOCIAL detetada")

    print("\n" + "=" * 65)
    print("Teste concluído.")
    print("=" * 65)
