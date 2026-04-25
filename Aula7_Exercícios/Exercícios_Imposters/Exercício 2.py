# Exercício 1 — Stub: lista de marcas (GET /api/marcas)


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
      }
    ]
  }'
  
curl "http://localhost:8000/api/cars?brand=Toyota"