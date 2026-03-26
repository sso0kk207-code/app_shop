from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Payment Service")

class PaymentRequest(BaseModel):
    order_id: int
    amount: float
    payment_method: str

class PaymentResponse(BaseModel):
    payment_id: int
    status: str
    message: str

@app.post("/payments", response_model=PaymentResponse)
async def create_payment(payment: PaymentRequest):
    """Создать платеж"""
    # Упрощенная логика обработки платежа
    payment_id = 1  # В реальности генерируется из БД
    
    return PaymentResponse(
        payment_id=payment_id,
        status="success",
        message=f"Платеж на сумму {payment.amount} руб. обработан"
    )

@app.get("/payments/{payment_id}")
async def get_payment(payment_id: int):
    """Получить информацию о платеже"""
    return {
        "payment_id": payment_id,
        "status": "completed",
        "amount": 1000.0
    }
