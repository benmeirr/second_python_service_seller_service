from typing import Optional, List

from model.item import Item
from repository.database import database

TABLE_NAME = "item"


async def get_item_by_id(item_id: int) -> Optional[Item]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:item_id"
    result = await database.fetch_one(query, values={"item_id": item_id})
    if result:
        return Item(**result)
    else:
        return None


async def get_all_items() -> List[Item]:
    query = f"SELECT * FROM {TABLE_NAME}"
    results = await database.fetch_all(query)
    return [Item(**result) for result in results]


async def create_item(item: Item) -> int:
    query = f"""
        INSERT INTO {TABLE_NAME} (seller_id, item_name, price)
        VALUES (:seller_id, :item_name, :price)
    """
    values = {
        "seller_id": item.id,
        "item_name": item.item_name,
        "price": item.price,
    }
    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")
    return last_record_id[0] if last_record_id else None


async def update_item(item_id: int, item: Item):
    query = f"""
        UPDATE {TABLE_NAME}
        SET seller_id = :seller_id, item_name = :item_name, price = :price
        WHERE id = :item_id
    """
    values = {
        "item_id": item_id,
        "seller_id": item.id,
        "item_name": item.item_name,
        "price": item.price,
    }
    await database.execute(query, values)


async def delete_item_by_id(item_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id=:item_id"
    await database.execute(query, values={"item_id": item_id})


async def get_lowest_price_item_by_name(item_name: str) -> Optional[Item]:
    query = f"""
        SELECT * FROM {TABLE_NAME}
        WHERE item_name = :item_name
        ORDER BY price ASC
        LIMIT 1
    """
    result = await database.fetch_one(query, values={"item_name": item_name})
    if result:
        return Item(**result)
    else:
        return None


