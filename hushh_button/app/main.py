
from fastapi import FastAPI
from app.routes.hushh_routes import router as hushh_router

app = FastAPI()

app.include_router(hushh_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Hushh Button Service"}
