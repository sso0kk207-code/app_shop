from dotenv import load_dotenv
import os

# Загрузка переменных из .env файла
load_dotenv()

# Конфигурация из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
REDIS_URL = os.getenv("REDIS_URL")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
