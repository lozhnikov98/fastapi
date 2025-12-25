from typing import List

from app.schemas.item import Item

# Простейшее хранилище в памяти процесса.
items_db: List[Item] = []
_id_counter = 1


def get_next_id() -> int:
    """Генерирует следующий уникальный ID."""
    global _id_counter
    value = _id_counter
    _id_counter += 1
    return value


def get_all_items() -> List[Item]:
    """Возвращает все элементы."""
    return items_db


def get_item_by_id(item_id: int) -> Item | None:
    """Возвращает элемент по ID или None, если не найден."""
    for item in items_db:
        if item.id == item_id:
            return item
    return None


def create_item(item: Item) -> Item:
    """Создает новый элемент."""
    items_db.append(item)
    return item


def update_item(item_id: int, updated_item: Item) -> Item:
    """Обновляет элемент."""
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db[idx] = updated_item
            return updated_item
    raise ValueError(f"Item with id {item_id} not found")


def delete_item(item_id: int) -> bool:
    """Удаляет элемент. Возвращает True, если элемент был удален."""
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(idx)
            return True
    return False

