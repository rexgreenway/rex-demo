from fastapi import FastAPI

app = FastAPI()

print("HELLo")


@app.get("/")
async def root():
    return {"message": "Hello World"}
