from fastapi import FastAPI, Response
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/", status_code=200)
def home():
    return FileResponse('index.html')
