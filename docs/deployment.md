# Развертывание

```bash
# Docker локально
docker-compose up -d

# Kubernetes
kubectl create namespace sfmshop && \
kubectl create secret generic db-pass --from-literal=password=PASS -n sfmshop && \
kubectl apply -f k8s/deployment.yaml -n sfmshop

## Откат

```bash
kubectl rollout undo deployment/api && \
cd migrations && alembic downgrade -1 && \
pg_restore -U postgres -d db backup.sql
```
