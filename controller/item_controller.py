from fastapi import APIRouter, HTTPException
from typing import List

from model.item import Item
from service import item_service

router = APIRouter(
    prefix="/item",
    tags=["item"]
)


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = await item_service.get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Item with id: {item_id} not found")
    return item


@router.post("/", response_model=Item)
async def create_item(item: Item):
    item_id = await item_service.create_item(item)
    return await item_service.get_item_by_id(item_id)


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    existing_item = await item_service.get_item_by_id(item_id)
    if not existing_item:
        raise HTTPException(status_code=404, detail=f"Can't update item with id: {item_id}, item not found")
    await item_service.update_item(item_id, item)
    return await item_service.get_item_by_id(item_id)


@router.delete("/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    existing_item = await item_service.get_item_by_id(item_id)
    if not existing_item:
        raise HTTPException(status_code=404, detail=f"Item with id: {item_id} not found")
    await item_service.delete_item_by_id(item_id)
    return existing_item


@router.get("/", response_model=List[Item])
async def get_items():
    return await item_service.get_all_items()


@router.get("/search/", response_model=Item)
async def get_lowest_price_item_by_name(item_name: str):
    item = await item_service.get_lowest_price_item_by_name(item_name)
    if not item:
        raise HTTPException(status_code=404, detail=f"No items found with name: {item_name}")
    return item


