from typing import List, Optional

from fastapi import FastAPI, HTTPException, Path, status
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., description="Название сущности", min_length=1, max_length=100)
    description: Optional[str] = Field(None, description="Произвольное описание", max_length=500)
    price: float = Field(..., description="Стоимость, число > 0", gt=0)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, description="Название сущности", min_length=1, max_length=100)
    description: Optional[str] = Field(None, description="Произвольное описание", max_length=500)
    price: Optional[float] = Field(None, description="Стоимость, число > 0", gt=0)


class Item(ItemBase):
    id: int = Field(..., description="Уникальный идентификатор")


app = FastAPI()

# Простейшее хранилище в памяти процесса.
items_db: List[Item] = []
_id_counter = 1


def _get_next_id() -> int:
    global _id_counter
    value = _id_counter
    _id_counter += 1
    return value


@app.get(
    "/list",
    response_model=List[Item],
    summary="Получить список сущностей",
    status_code=status.HTTP_200_OK,
)
def list_items() -> List[Item]:
    return items_db


@app.get(
    "/get/{item_id}",
    response_model=Item,
    summary="Получить одну сущность",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Сущность не найдена"}},
)
def get_item(
    item_id: int = Path(..., description="ID сущности", ge=1),
) -> Item:
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.post(
    "/create",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    summary="Создать сущность",
)
def create_item(payload: ItemCreate) -> Item:
    new_item = Item(id=_get_next_id(), **payload.dict())
    items_db.append(new_item)
    return new_item


@app.put(
    "/update/{item_id}",
    response_model=Item,
    summary="Изменить данные сущности",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Сущность не найдена"}},
)
def update_item(
    payload: ItemUpdate,
    item_id: int = Path(..., description="ID сущности", ge=1),
) -> Item:
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            updated_data = item.dict()
            for field, value in payload.dict(exclude_unset=True).items():
                updated_data[field] = value
            updated_item = Item(**updated_data)
            items_db[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.delete(
    "/delete/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить сущность",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Сущность не найдена"}},
)
def delete_item(
    item_id: int = Path(..., description="ID сущности", ge=1),
) -> None:
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(idx)
            return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


