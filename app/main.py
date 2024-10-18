import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .porfolio import photography_router
from .software import bv_router, pl_router

# Establish Core API
app = FastAPI()

# Establish Logger
logger = logging.getLogger(__name__)

origins = [
    "http://127.0.0.1:5173",
    "https://rexgreenway.github.io/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SOFTWARE ROUTES
app.include_router(pl_router)
app.include_router(bv_router)

# PORTFOLIO ROUTES
app.include_router(photography_router)

print("RUNNING API!!!")


@app.get("/")
async def root():
    return {"message": "Welcome to the Rex Demo API"}
