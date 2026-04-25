# Exercício 9 — Stub: temperatura — criação com field presente (POST /api/temperature com value)


{
  "predicates": [{"equals": {"method": "POST", "path": "/api/temperature", "headers": {"Content-Type": "application/json"}}}, {"contains": {"body": "\"value\""}}],
  "responses": [{"is": {"statusCode": 201, "headers": {"Content-Type": "application/json"}, "body": {"status": "created"}}}]
}

curl -X POST http://localhost:8000/api/temperature \
  -H "Content-Type: application/json" \
  -d '{"sensor_id":1,"value":25.5}'