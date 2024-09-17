from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .polylatlib import pl_router

# Establish Core API
app = FastAPI()

origins = [
    "http://localhost",
    "https://rexgreenway.github.io/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Sub-routers
app.include_router(pl_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Rex Demo API"}
