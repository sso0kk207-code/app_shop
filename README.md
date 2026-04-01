# SFMShop

Интернет-магазин на Python.

## Запуск

```bash
# Python
git clone <repo> && cd app_shop
python3.12 -m venv venv && source venv/bin/activate
pip install -r requirements.txt && cp .env.exmaple .env
uvicorn src.main:app --reload

# Docker
docker-compose up -d
```

## Тесты

```bash
pytest
pytest --cov=src --cov-report=html
```

## Структура

```
src/    - API, models, services, database, utils
tests/  - Тесты
docs/   - Документация
```
