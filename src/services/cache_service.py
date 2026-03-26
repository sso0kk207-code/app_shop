import redis

# Подключение к Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def get_cached_products():
    """Получить список товаров из кэша"""
    cached = redis_client.get("products:all")
    if cached:
        import json
        return json.loads(cached)
    return None

def set_cached_products(products, ttl=3600):
    """Сохранить список товаров в кэш с TTL"""
    import json
    redis_client.setex("products:all", ttl, json.dumps(products))
    print(f"Товары сохранены в кэш на {ttl} секунд")

def get_user_session(user_id):
    """Получить сессию пользователя из Redis"""
    return redis_client.get(f"session:{user_id}")

def set_user_session(user_id, session_data, ttl=1800):
    """Сохранить сессию пользователя в Redis"""
    import json
    redis_client.setex(f"session:{user_id}", ttl, json.dumps(session_data))
    print(f"Сессия пользователя {user_id} сохранена на {ttl} секунд")
