# Exercício 14 — Stub genérico para POST com Content-Type obrigatório


{
  "predicates": [{"equals": {"method": "POST"}}],
  "responses": [{"is": {"statusCode": 415, "headers": {"Content-Type": "application/json"}, "body": {"error": "unsupported_media_type", "message": "Content-Type application/json is required"}}}]
}

curl -X POST http://localhost:8000/api/qualquer-coisa \
  -d '{"teste":1}'