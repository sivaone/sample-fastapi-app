from fastapi import FastAPI, HTTPException

from datetime import datetime, UTC
from os import environ
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    fname: str = Field(min_length=5, max_length=10)
    lname: str = Field(min_length=4, max_length=10)
    city: str = Field(min_length=3, max_length=10)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/info")
async def info():
    return {
        "version": "1.0",
        "time": datetime.now(UTC),
        'user': environ.get('USERNAME', 'unknown'),
    }


@app.get("/search")
async def search(fname: str, lname: str, city: str = None):
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")



    return {
        "fullName": fname + " " + lname + " " + city,
    }

@app.post("/users")
async def create_user(user: User):
    return {
        "id": 1,
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
