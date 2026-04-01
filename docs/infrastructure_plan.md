# Инфраструктура

```
Nginx → API (3-10) → PostgreSQL + Redis
```

## Компоненты

- Nginx - балансировка, HTTPS
- FastAPI - 3-10 реплик
- PostgreSQL - Primary + Standby
- Redis - кэш, сессии

## Deploy

```bash
docker-compose up -d
aws ecs create-service --cluster sfmshop --service-name api --desired-count 3
kubectl apply -f k8s/deployment.yaml
gcloud run deploy app --image gcr.io/PROJECT_ID/app
```

## Масштабирование

- Горизонтальное: реплики
- Вертикальное: CPU/RAM
- Автоматическое: по метрикам

## Безопасность

- Firewall + VPC
- HTTPS (Let's Encrypt)
- JWT + secrets в .env
