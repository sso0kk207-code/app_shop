# Тестирование

```bash
pytest
pytest --cov=src
```

## Примеры

```python
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_orders():
    assert client.get("/api/orders").status_code == 200
    assert client.post("/api/orders", json={}).status_code in (201, 422)
```
