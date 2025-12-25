# FastAPI CRUD приложение

Простое REST API приложение на FastAPI с полным набором CRUD-операций для работы с сущностями. Данные хранятся в памяти процесса.

## Структура проекта

```
fastapi/
├── app/
│   ├── __init__.py
│   ├── database.py          # Хранилище данных и функции работы с БД
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── item.py          # Pydantic модели (Item, ItemCreate, ItemUpdate)
│   └── routers/
│       ├── __init__.py
│       └── items.py         # Роутеры для работы с items
├── main.py                  # Точка входа приложения
├── requirements.txt         # Зависимости проекта
└── readme.md               # Документация
```

## Требования

- Python 3.10+
- FastAPI
- Uvicorn

## Установка и запуск

### 1. Создание виртуального окружения

```bash
python -m venv venv
```

### 2. Активация виртуального окружения

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск приложения

```bash
uvicorn main:app --reload
```

Приложение будет доступно по адресу: `http://localhost:8000`

## API Эндпоинты

Все эндпоинты имеют префикс `/api`:

- `GET /api/list` — получить список всех сущностей
- `GET /api/get/{item_id}` — получить сущность по ID
- `POST /api/create` — создать новую сущность
- `PUT /api/update/{item_id}` — обновить существующую сущность
- `DELETE /api/delete/{item_id}` — удалить сущность

### Примеры запросов

#### Создание сущности
```bash
POST /api/create
Content-Type: application/json

{
  "name": "Пример",
  "description": "Описание сущности",
  "price": 99.99
}
```

#### Получение списка
```bash
GET /api/list
```

#### Получение по ID
```bash
GET /api/get/1
```

#### Обновление сущности
```bash
PUT /api/update/1
Content-Type: application/json

{
  "name": "Обновленное название",
  "price": 149.99
}
```

#### Удаление сущности
```bash
DELETE /api/delete/1
```

## Документация API

После запуска приложения доступна интерактивная документация:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`