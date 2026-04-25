# Exercício 6 — Stub: criar utilizador (email duplicado) (POST /api/users com email específico)


curl -X PUT http://localhost:2525/imposters/8000 \
  -H "Content-Type: application/json" \
  -d '{
    "port": 8000,
    "protocol": "http",
    "stubs": [
      {
        "predicates": [{"equals": {"method": "GET", "path": "/api/marcas"}}],
        "responses": [{"is": {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": {"marcas": ["Toyota", "Audi", "Ford", "Volvo", "Honda"]}}}]
      },
      {
        "predicates": [{"equals": {"method": "GET", "path": "/api/cars"}}, {"contains": {"query": "brand=Toyota"}}],
        "responses": [{"is": {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": {"brand": "Toyota", "results": [{"id": 1, "modelo": "Corolla", "preco": 25000}]}}}]
      },
      {
        "predicates": [{"equals": {"method": "GET", "path": "/api/cars"}}],
        "responses": [{"is": {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": {"results": []}}}]
      },
      {
        "predicates": [{"equals": {"method": "POST", "path": "/api/login", "headers": {"Content-Type": "application/json"}, "body": {"username": "admin", "password": "secret"}}}],
        "responses": [{"is": {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": {"status": "ok", "token": "validtoken"}}}]
      },
      {
        "predicates": [{"equals": {"method": "POST", "path": "/api/login", "headers": {"Content-Type": "application/json"}}}],
        "responses": [{"is": {"statusCode": 401, "headers": {"Content-Type": "application/json"}, "body": {"error": "invalid_credentials"}}}]
      },
      {
        "predicates": [{"equals": {"method": "POST", "path": "/api/users", "headers": {"Content-Type": "application/json"}}}, {"contains": {"body": "\"email\":\"exists@example.com\""}}],
        "responses": [{"is": {"statusCode": 409, "headers": {"Content-Type": "application/json"}, "body": {"error": "email_exists", "message": "Email already exists"}}}]
      }
    ]
  }'
  
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{"email":"exists@example.com","name":"Teste"}'


