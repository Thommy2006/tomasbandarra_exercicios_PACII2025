# Exercício 8 — Stub: temperatura — campo obrigatório (POST /api/temperature sem field)


curl -X PUT http://localhost:2525/imposters/8000 \
  -H "Content-Type: application/json" \
  -d '{
    "port": 8000,
    "protocol": "http",
    "stubs": [
      ... (stubs anteriores) ...,
      {
        "predicates": [{"equals": {"method": "POST", "path": "/api/temperature", "headers": {"Content-Type": "application/json"}}}, {"not": {"contains": {"body": "\"value\""}}}],
        "responses": [{"is": {"statusCode": 400, "headers": {"Content-Type": "application/json"}, "body": {"error": "missing_field", "message": "value is required"}}}]
      }
    ]
  }'
  
curl -X POST http://localhost:8000/api/temperature \
  -H "Content-Type: application/json" \
  -d '{"sensor_id":1}'