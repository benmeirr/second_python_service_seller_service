from typing import Optional, List

from model.seller import Seller
from repository import seller_repository


async def get_seller_by_id(seller_id: int) -> Optional[Seller]:
    return await seller_repository.get_seller_by_id(seller_id)


async def get_all_sellers() -> List[Seller]:
    return await seller_repository.get_all_sellers()


async def create_seller(seller: Seller) -> int:
    return await seller_repository.create_seller(seller)


async def update_seller(seller_id: int, seller: Seller):
    await seller_repository.update_seller(seller_id, seller)


async def delete_seller_by_id(seller_id: int):
    await seller_repository.delete_seller_by_id(seller_id)
