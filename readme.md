# FastAPI CRUD пример

Простое приложение FastAPI с CRUD-эндпоинтами и хранением данных в памяти процесса.

## Требования
- Python 3.10+

## Установка и запуск
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

## Эндпоинты
- `GET /list` — список сущностей.
- `GET /get/{item_id}` — получение сущности.
- `POST /create` — создание сущности.
- `PUT /update/{item_id}` — обновление сущности.
- `DELETE /delete/{item_id}` — удаление сущности.

Документация доступна на `/docs` (Swagger UI) и `/redoc`.

