from fastapi import FastAPI
from .database import Base, engine
from .routers import router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(router)
