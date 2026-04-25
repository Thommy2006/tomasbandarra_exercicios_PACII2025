# Exercício 10 — Stub: tarefas duplicadas (POST /api/tasks com title "duplicate")


{
  "predicates": [{"equals": {"method": "POST", "path": "/api/tasks", "headers": {"Content-Type": "application/json"}}}, {"contains": {"body": "\"title\":\"duplicate\""}}],
  "responses": [{"is": {"statusCode": 409, "headers": {"Content-Type": "application/json"}, "body": {"error": "duplicate_task"}}}]
}

curl -X POST http://localhost:8000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"duplicate"}'