# Payment Service

Микросервис для обработки платежей в проекте SFMShop.

## Описание

Микросервис для обработки платежей, который работает независимо от основного сервиса.

## Запуск

```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8001
```

## API Endpoints

- POST /payments - создание платежа
- GET /payments/{payment_id} - получение информации о платеже
