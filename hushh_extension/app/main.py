
from fastapi import FastAPI
from app.routes.extension_routes import router as extension_router

app = FastAPI()

app.include_router(extension_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Hushh Extension Service"}
