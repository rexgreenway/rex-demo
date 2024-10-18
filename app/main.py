import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .portfolio import photography_router

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

# PORTFOLIO ROUTES
app.include_router(photography_router)
