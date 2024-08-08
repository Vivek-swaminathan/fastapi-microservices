
from fastapi import FastAPI
from app.routes.wallet_routes import router as wallet_router

app = FastAPI()

app.include_router(wallet_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Wallet App Service"}
