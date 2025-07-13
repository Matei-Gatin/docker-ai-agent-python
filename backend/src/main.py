from fastapi import FastAPI
import os

app = FastAPI()

MY_PROJECT = os.environ.get("MY_PROJECT") or "This is my project"
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplemented(f'API KEY was not set')

@app.get("/")
def read_index():
    return {"message": "no yes", "project": MY_PROJECT}

