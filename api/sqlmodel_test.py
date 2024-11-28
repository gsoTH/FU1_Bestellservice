from sqlmodel import Field, Session, SQLModel, create_engine, select, Relationship

class Item(SQLModel, table=True):
#   order_id: int = Field(default=None, foreign_key="tabelle.spalte", primary_key=True)
    order_id: int = Field(default=None, foreign_key="orders.id", primary_key=True)
    pizza_id: int = Field(default=None, foreign_key="pizza.id", primary_key=True)
    amount: int


class Pizza(SQLModel, table=True):
    id:  int = Field(primary_key=True)
    name: str
    toppings: str
    price: float

    ordered: list["Order"] = Relationship(back_populates="items", link_model=Item)

class Order(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    phone: str

    items: list[Item] = Relationship(back_populates="ordered", link_model=Item)



sqlite_file_name = "../testdata/test_database.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True) #echo=True will show SQL output.

def select_pizza():
    with Session(engine) as session:
        statement = select(Pizza)
        results = session.exec(statement)
        for pizza in results:
            print(pizza)

if __name__ == "__main__":
    select_pizza()
