# Exercício 11 — Stub: criação de tarefa com sucesso (POST /api/tasks)


{
  "predicates": [{"equals": {"method": "POST", "path": "/api/tasks", "headers": {"Content-Type": "application/json"}}}],
  "responses": [{"is": {"statusCode": 201, "headers": {"Content-Type": "application/json", "Location": "/api/tasks/456"}, "body": {"id": 456, "status": "created"}}}]
}

curl -X POST http://localhost:8000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Nova tarefa"}'