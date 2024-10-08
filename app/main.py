from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .porfolio import photography_router
from .software import bv_router, pl_router

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

# SOFTWARE ROUTES
app.include_router(pl_router)
app.include_router(bv_router)

# PORTFOLIO ROUTES
app.include_router(photography_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Rex Demo API"}
