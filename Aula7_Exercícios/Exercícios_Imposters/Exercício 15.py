# Exercício 15 — Stub genérico para GET (fallback 404)


{
  "predicates": [{"equals": {"method": "GET"}}],
  "responses": [{"is": {"statusCode": 404, "headers": {"Content-Type": "application/json"}, "body": {"error": "not_found"}}}]
}

curl http://localhost:8000/caminho-que-nao-existe