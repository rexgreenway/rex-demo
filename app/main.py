from fastapi import FastAPI

from .polylatlib import pl_router

# Establish Core API
app = FastAPI()

# Register Sub-routers
app.include_router(pl_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Rex Demo API"}
