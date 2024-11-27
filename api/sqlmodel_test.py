from sqlmodel import Field, Session, SQLModel, create_engine, select

class Pizza(SQLModel, table=True):
    id:  int | None = Field(primary_key=True)
    name: str
    toppings: str
    price: float


class Order(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str
    phone: str

#class Item(SQLModel, table=True):



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
