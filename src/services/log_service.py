from pymongo import MongoClient
from datetime import datetime

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['sfmshop']
logs_collection = db['logs']

def save_log(level, message, metadata=None):
    """Сохранить лог в MongoDB"""
    log_entry = {
        "level": level,
        "message": message,
        "timestamp": datetime.now(),
        "metadata": metadata or {}
    }
    logs_collection.insert_one(log_entry)
    print(f"Лог сохранен: {level} - {message}")

def get_logs(level=None, start_date=None, end_date=None):
    """Получить логи из MongoDB"""
    query = {}
    
    if level:
        query["level"] = level
    
    if start_date or end_date:
        query["timestamp"] = {}
        if start_date:
            query["timestamp"]["$gte"] = start_date
        if end_date:
            query["timestamp"]["$lte"] = end_date
    
    logs = logs_collection.find(query).sort("timestamp", -1)
    return list(logs)

def get_error_logs():
    """Получить только ошибки"""
    return get_logs(level="error")
