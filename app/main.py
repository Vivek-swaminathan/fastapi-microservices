
from fastapi import FastAPI
from app.routes.main_routes import router as main_router

app = FastAPI()

app.include_router(main_router)

@app.get("/")
async def root():
    return {"message": "This is the main service"}
