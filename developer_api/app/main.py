
from fastapi import FastAPI
from app.routes.developer_routes import router as developer_router

app = FastAPI()

app.include_router(developer_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Developer API Service"}
