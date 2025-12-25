from typing import List

from fastapi import APIRouter, HTTPException, Path, status

from app.database import (
    create_item as db_create_item,
    delete_item as db_delete_item,
    get_all_items,
    get_item_by_id,
    get_next_id,
    update_item as db_update_item,
)
from app.schemas.item import Item, ItemCreate, ItemUpdate

router = APIRouter(prefix="/api", tags=["items"])


@router.get(
    "/list",
    response_model=List[Item],
    summary="Получить список сущностей",
    status_code=status.HTTP_200_OK,
)
def list_items() -> List[Item]:
    """Возвращает список всех сущностей."""
    return get_all_items()


@router.get(
    "/get/{item_id}",
    response_model=Item,
    summary="Получить одну сущность",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Сущность не найдена"}},
)
def get_item(
    item_id: int = Path(..., description="ID сущности", ge=1),
) -> Item:
    """Возвращает сущность по ID."""
    item = get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item


@router.post(
    "/create",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    summary="Создать сущность",
)
def create_item(payload: ItemCreate) -> Item:
    """Создает новую сущность."""
    new_item = Item(id=get_next_id(), **payload.model_dump())
    return db_create_item(new_item)


@router.put(
    "/update/{item_id}",
    response_model=Item,
    summary="Изменить данные сущности",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Сущность не найдена"}},
)
def update_item(
    payload: ItemUpdate,
    item_id: int = Path(..., description="ID сущности", ge=1),
) -> Item:
    """Обновляет данные сущности."""
    existing_item = get_item_by_id(item_id)
    if existing_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    
    updated_data = existing_item.model_dump()
    for field, value in payload.model_dump(exclude_unset=True).items():
        updated_data[field] = value
    updated_item = Item(**updated_data)
    
    return db_update_item(item_id, updated_item)


@router.delete(
    "/delete/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить сущность",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Сущность не найдена"}},
)
def delete_item(
    item_id: int = Path(..., description="ID сущности", ge=1),
) -> None:
    """Удаляет сущность."""
    if not db_delete_item(item_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return None

