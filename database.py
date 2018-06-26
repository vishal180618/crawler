from requests import Session
from sqlalchemy import Column, Integer, String, Numeric,ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


Base = declarative_base()


class Information(Base):
    __tablename__ = 'information'
    id = Column(Integer, primary_key=True)
    title=Column(String(1500))
    description=Column(String(1500))
    date=Column(String(50))
    location=Column(String(1500),nullable=True)
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    # name = Column(String(250), nullable=False)
    # sqlite_autoincrement = True

#
# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///crawler1.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)