from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from sqlmodel import Session, SQLModel, create_engine, select

# Definiere das SQLite-Datenbankmodell
class Pizza(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: float

class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    customer_name: str
    phone_number: str
    total: float

# Erstelle eine Datenbankverbindung
DATABASE_URL = "sqlite:///./test.db"  # Lokale SQLite-Datei
engine = create_engine(DATABASE_URL, echo=True)

# Erstelle die Datenbanktabellen
SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI()


class Pizza(BaseModel):
    pizza_id: int = Field(gt=0)
    quantity: int = Field(gt=0)
    
class OrderRequest(BaseModel):
    customer_name: str = Field(min_length=1)
    phone_number: str = Field(min_length=1)
    items: list[Pizza]
        
class OrderResponse(BaseModel):
    order_number: int
    customer_name: str
    phone_number: str
    total: float
    items: list[Pizza]



@app.get("/", status_code=200)
def home():
    return FileResponse('index.html')

@app.get("/menu", status_code=200)
def get_menu():
    return FileResponse('testdata/get_menue.json')

@app.post("/order/", status_code=201)
def post_order_request(order: OrderRequest, session: Session = get_session()) -> OrderResponse:
    # Berechne den Gesamtpreis für die Bestellung
    pizzas = session.exec(select(Pizza).where(Pizza.id.in_(order.items))).all()
    total = sum(pizza.price for pizza in pizzas)

    db_order = Order(
        customer_name=order.customer_name,
        phone_number=order.phone_number,
        total=total,
    )

    session.add(db_order)
    session.commit()
    session.refresh(db_order)

    # Füge die bestellten Pizzen zur Bestellung hinzu
    db_order_items = []
    for pizza in pizzas:
        db_order_items.append({"pizza_id": pizza.id, "order_id": db_order.id})
    
    session.commit()

    return db_order