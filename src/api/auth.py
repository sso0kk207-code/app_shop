from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer

security = HTTPBearer()

def verify_token(token: str = Depends(security)):
    """Проверка JWT токена"""
    # Упрощенная проверка токена
    if not token:
        raise HTTPException(status_code=401, detail="Токен не предоставлен")
    return token
