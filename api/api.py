from fastapi import FastAPI, Response, status
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
def home():
    return FileResponse('index.html')


@app.get('/freieTische', status_code=200)
def freie_tische(zeitpunkt: str, response: Response):
    # TODO wunschzeitpunkt auf nächste halbe Stunde aufrunden (18:00 --> 18:30)
    # TODO SQLite Datenbank erzeugen (create_buchungssystem.sql) und einbinden
    # TODO Abfrage an SQLite Datenbank absetzen
    # TODO Ergebnis der Abfrage als JSON zurückgeben
    # TODO Überprüfen, ob Parameter dem Muster yyyy-mm-dd hh:mm entspricht
    
    return zeitpunkt
    
