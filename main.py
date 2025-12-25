from fastapi import FastAPI

from app.routers import items

app = FastAPI(title="FastAPI Items API", version="1.0.0")

# Подключаем роутеры
app.include_router(items.router)


