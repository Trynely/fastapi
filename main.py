import asyncpg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Создаем FastAPI приложение
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173", # Пример URL для React приложения
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

# Конфигурация подключения к базе данных PostgreSQL
DATABASE_URL = "postgresql://postgres:tigerking0506@localhost/shoes"

# Функция для подключения к базе данных
async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

# Функция для получения данных из таблицы
@app.get("/items/")
async def get_items():
    conn = await connect_to_db()
    try:
        # Выполнение запроса к базе данных
        rows = await conn.fetch("SELECT * FROM api_things")
        # Преобразование результата в список словарей
        items = [dict(row) for row in rows]
        return items
    finally:
        await conn.close()
