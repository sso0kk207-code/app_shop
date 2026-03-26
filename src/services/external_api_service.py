import requests

def get_exchange_rate():
    """Получить курс валют из внешнего API"""
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Ошибка при получении курса валют: {e}")
        return None
