# Exercício 12 — Stub: autenticação (POST /api/auth)


{
  "predicates": [{"equals": {"method": "POST", "path": "/api/auth", "headers": {"Content-Type": "application/json"}, "body": {"username": "user1", "password": "pass1"}}}],
  "responses": [{"is": {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": {"token": "auth_token_123", "expires_in": 3600}}}]
},
{
  "predicates": [{"equals": {"method": "POST", "path": "/api/auth", "headers": {"Content-Type": "application/json"}}}],
  "responses": [{"is": {"statusCode": 401, "headers": {"Content-Type": "application/json"}, "body": {"error": "invalid_credentials"}}}]
}


curl -X POST http://localhost:8000/api/auth \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","password":"pass1"}'


curl -X POST http://localhost:8000/api/auth \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","password":"errado"}'