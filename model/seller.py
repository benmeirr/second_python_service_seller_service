from typing import Optional

from pydantic import BaseModel

from model.seller_status import SellerStatus


class Seller(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    status: SellerStatus


