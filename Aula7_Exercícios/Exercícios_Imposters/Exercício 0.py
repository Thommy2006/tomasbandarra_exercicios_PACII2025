# Exercício 0 — Preparação inicial


curl -X POST http://localhost:2525/imposters \
  -H "Content-Type: application/json" \
  -d '{"port": 8000, "protocol": "http", "stubs": []}'
  
curl -X GET http://localhost:8000/qualquer-coisa