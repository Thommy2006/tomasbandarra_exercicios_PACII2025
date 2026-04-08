# LAB 1 – Sistema de Chat com Deteção de Dados Pessoais (GDPR)

Sistema de chat multiutilizadores em Python com deteção de dados pessoais conforme o GDPR
e registo de tentativas de engenharia social.

---

## Estrutura do Projeto

```
chat_gdpr/
├── server.py           # Servidor central de chat
├── client.py           # Cliente de chat (CLI)
├── gdpr_detector.py    # Módulo de deteção de dados pessoais

```

---

## Requisitos

- Python 3.10+
- Sem dependências externas (apenas módulos da biblioteca padrão)

---

## Como Executar

### 1. Iniciar o Servidor

```bash
python server.py
```

O servidor fica à escuta em `0.0.0.0:9999` por defeito.

### 2. Iniciar um Cliente

```bash
python client.py
```

Ou indicando host e porta personalizados:

```bash
python client.py 192.168.1.10 9999
```

Cada cliente deve ser executado num terminal separado.

---

## Comandos do Cliente

| Comando             | Descrição                                |
|---------------------|------------------------------------------|
| `exit`              | Desligar do servidor                     |
| `!online`           | Listar utilizadores online               |
| `@nome mensagem`    | Enviar mensagem privada (DM) a um user   |

---

## Deteção de Dados Pessoais (GDPR)

O módulo `gdpr_detector.py` usa **expressões regulares** para detetar:

| Tipo              | Exemplos                              |
|-------------------|---------------------------------------|
| E-mail            | `user@exemplo.pt`                     |
| Número de telefone| `912345678`, `+351 91 234 5678`       |
| Endereço IP       | `192.168.1.1`                         |
| Data de nascimento| `01/01/1990`, `31-12-99`              |
| Cartão de crédito | `1234 5678 9012 3456`                 |
| Nome completo     | `João Bravo Silva`                    |

Se dados pessoais forem detetados:
1. A mensagem é **bloqueada** (não enviada).
2. O utilizador recebe um **alerta GDPR**.
3. A ocorrência é **guardada** em `personal_data_log.json`.





## Arquitetura

```
  ┌─────────┐        socket TCP        ┌──────────────────────┐
  │ cliente │ ──────────────────────►  │                      │
  │  (CLI)  │ ◄──────────────────────  │   Servidor Central   │
  └─────────┘                          │   (multithreaded)    │
  ┌─────────┐                          │                      │
  │ cliente │ ──────────────────────►  │  ┌────────────────┐  │
  │  (CLI)  │ ◄──────────────────────  │  │ gdpr_detector  │  │
  └─────────┘                          │  └────────────────┘  │
       …                               └──────────────────────┘

