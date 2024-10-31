from typing import Optional, List

from model.seller import Seller
from repository.database import database

TABLE_NAME = "seller"


async def get_seller_by_id(seller_id: int) -> Optional[Seller]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:seller_id"
    result = await database.fetch_one(query, values={"seller_id": seller_id})
    if result:
        return Seller(**result)
    else:
        return None


async def get_all_sellers() -> List[Seller]:
    query = f"SELECT * FROM {TABLE_NAME}"
    results = await database.fetch_all(query)
    return [Seller(**result) for result in results]


async def create_seller(seller: Seller) -> int:
    query = f"""
        INSERT INTO {TABLE_NAME} (name, email, status)
        VALUES (:name, :email, :status)
    """
    values = {"name": seller.name, "email": seller.email, "status": seller.status}
    async with database.transaction():
        await database.execute(query, values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")
    return last_record_id[0] if last_record_id else None


async def update_seller(seller_id: int, seller: Seller):
    query = f"""
        UPDATE {TABLE_NAME}
        SET name = :name, email = :email, status = :status 
        WHERE id = :seller_id
    """
    values = {
        "seller_id": seller_id,
        "name": seller.name,
        "email": seller.email,
        "status": seller.status,
    }
    await database.execute(query, values)


async def delete_seller_by_id(seller_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id=:seller_id"
    await database.execute(query, values={"seller_id": seller_id})
