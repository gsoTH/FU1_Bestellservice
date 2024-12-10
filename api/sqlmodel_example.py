from sqlmodel import Field, Relationship, Session, SQLModel, create_engine


class Order2Pizza(SQLModel, table=True):
    order_id: int | None = Field(default=None, foreign_key="order.id", primary_key=True)
    pizza_id: int | None = Field(default=None, foreign_key="pizza.id", primary_key=True)
    amount: int = Field(default=1)


class Pizza(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    toppings: str = Field(default=None)
    price: int = Field(default=900)

    orders: list["Order"] = Relationship(back_populates="items", link_model=Order2Pizza)


class Order(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    phone: str = Field()

    items: list[Pizza] = Relationship(back_populates="orders", link_model=Order2Pizza)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
sqlite_url = "sqlite:///:memory:"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_orders():
    with Session(engine) as session:
        mario = Pizza(name="Mario", toppings="Käse, Tomatensauce", price=900)
        luigi = Pizza(name="Luigi", toppings="Käse, Spinat", price=1250)

        bestellung_1 = Order(
            name="Max Mustermann",
            phone="0221-0800123",
            items=[mario, luigi],
        )

        bestellung_2 = Order(
            name="Max Mustermann",
            phone="0221-0800123",
            items=[],
        )

        mehrere_pizzen = Order2Pizza(
            order = bestellung_2,
            pizza = mario,
            amount = 2
        )

        #https://sqlmodel.tiangolo.com/tutorial/many-to-many/link-with-extra-fields/#create-relationships

        session.add(mario)
        session.add(luigi)
        session.add(bestellung_1)
        session.add(mehrere_pizzen)
        session.commit()

        #session.refresh(hero_deadpond)
        #print("Deadpond:", hero_deadpond)
        #print("Deadpond teams:", hero_deadpond.teams)



def main():
    create_db_and_tables()
    create_orders()


if __name__ == "__main__":
    main()