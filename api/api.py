from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field


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
def post_order_request(order: OrderRequest) -> OrderResponse:
    exampleOrderResponse =  OrderResponse(  order_number=42,
                                            customer_name=order.customer_name, 
                                            phone_number = order.phone_number, 
                                            total = 3.5,
                                            items = order.items
                                            )
    return exampleOrderResponse