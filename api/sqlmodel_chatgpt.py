from sqlmodel import SQLModel, Field, Relationship, Session, create_engine
from typing import List, Optional

'''
# Die Zwischentabelle für die n:m-Beziehung
class StudentKurs(SQLModel, table=True):
    student_id: int = Field(foreign_key="student.id", primary_key=True)
    kurs_id: int = Field(foreign_key="kurs.id", primary_key=True)

# Das Student-Modell
class Student(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    kurse: List["Kurs"] = Relationship(back_populates="studenten", link_model=StudentKurs)

# Das Kurs-Modell
class Kurs(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    studenten: List[Student] = Relationship(back_populates="kurse", link_model=StudentKurs)
'''




class Parent(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    children: List["Child"] = Relationship(back_populates="parent")


class Child(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    parent: Parent = Relationship(back_populates="children") # muss vor parent_id festgelegt werden
    parent_id: int = Field(default=None, foreign_key="parent.id")


# Set up the database engine and session
sqlite_file_name = "database.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"
#sqlite_url = "sqlite:///:memory:"  # SQLite in-memory database
engine = create_engine(sqlite_url, echo=True)

# Create the tables in the database
SQLModel.metadata.create_all(engine)

# Create a session to interact with the database
def create_all():
    with Session(engine) as session:
        # Create a new Parent object
        parent = Parent(name="John Doe")

        session.add(parent)

        # Create new Child objects and associate them with the parent
        child1 = Child(name="Child 1", parent=parent)
        child2 = Child(name="Child 2", parent=parent)

        # Add the parent (which also adds the children because of the relationship)
        session.refresh(parent)

        # Commit the transaction to save the objects to the database
        session.commit()

        # Query the database to verify the data was inserted
        parents = session.get(Parent).all()
        for p in parents:
            print(f"Parent: {p.name}, Children: {[child.name for child in p.children]}")