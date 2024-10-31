from fastapi import FastAPI

from controller.seller_controller import router as seller_router
from controller.item_controller import router as item_router
from repository.database import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(seller_router)
app.include_router(item_router)