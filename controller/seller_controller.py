from fastapi import APIRouter, HTTPException
from typing import List

from model.seller import Seller
from service import seller_service

router = APIRouter(
    prefix="/seller",
    tags=["seller"]
)


@router.get("/{seller_id}", response_model=Seller)
async def get_seller_by_id(seller_id: int):
    seller = await seller_service.get_seller_by_id(seller_id)
    if not seller:
        raise HTTPException(status_code=404, detail=f"Seller with id: {seller_id} not found")
    return seller


@router.post("/", response_model=Seller)
async def create_seller(seller: Seller):
    seller_id = await seller_service.create_seller(seller)
    return await seller_service.get_seller_by_id(seller_id)


@router.put("/{seller_id}", response_model=Seller)
async def update_seller(seller_id: int, seller: Seller):
    existing_seller = await seller_service.get_seller_by_id(seller_id)
    if not existing_seller:
        raise HTTPException(status_code=404, detail=f"Can't update seller with id: {seller_id}, seller not found")
    await seller_service.update_seller(seller_id, seller)
    return await seller_service.get_seller_by_id(seller_id)


@router.delete("/{seller_id}", response_model=Seller)
async def delete_seller(seller_id: int):
    existing_seller = await seller_service.get_seller_by_id(seller_id)
    if not existing_seller:
        raise HTTPException(status_code=404, detail=f"Seller with id: {seller_id} not found")
    await seller_service.delete_seller_by_id(seller_id)
    return existing_seller


@router.get("/", response_model=List[Seller])
async def get_sellers():
    return await seller_service.get_all_sellers()
