from typing import Optional

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

