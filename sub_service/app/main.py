
from fastapi import FastAPI
from app.routes.sub_routes import router as sub_router

app = FastAPI()

app.include_router(sub_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Subservice"}
