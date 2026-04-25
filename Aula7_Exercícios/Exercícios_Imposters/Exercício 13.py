# Exercício 13 — Stub: recurso protegido / perfil (GET /api/profile com Authorization)


{
  "predicates": [{"equals": {"method": "GET", "path": "/api/profile", "headers": {"Authorization": "Bearer validtoken"}}}],
  "responses": [{"is": {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": {"username": "user1", "email": "user1@example.com"}}}]
},
{
  "predicates": [{"equals": {"method": "GET", "path": "/api/profile"}}],
  "responses": [{"is": {"statusCode": 403, "headers": {"Content-Type": "application/json"}, "body": {"error": "forbidden"}}}]
}


curl -X GET http://localhost:8000/api/profile \
  -H "Authorization: Bearer validtoken"


curl -X GET http://localhost:8000/api/profile