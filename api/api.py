from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/", status_code=200)
def home():
    return FileResponse('index.html')

@app.get("/menu", status_code=200)
def get_menu():
    return FileResponse('testdata/get_menue.json')

@app.post("/order/", status_code=201)
def post_order_request():
    # TODO JSON mit Pydantic vallidieren
    # TODO Beispiel-Response zurückgeben
    return None