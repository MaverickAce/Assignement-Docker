
from fastapi import FastAPI
from pyreadline3 import Readline
readline = Readline()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

