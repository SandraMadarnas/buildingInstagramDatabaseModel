from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
#engine = create_engine('sqlite:///sales.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship
#added:
from eralchemy2 import render_er

class Customer(Base):
   __tablename__ = 'customers'

   id = Column(Integer, primary_key = True)
   name = Column(String)
   address = Column(String)
   email = Column(String)

class Invoice(Base):
   __tablename__ = 'invoices'
   
   id = Column(Integer, primary_key = True)
   custid = Column(Integer, ForeignKey('customers.id'))
   invno = Column(Integer)
   amount = Column(Integer)
   customer = relationship("Customer", back_populates = "invoices")

Customer.invoices = relationship("Invoice", order_by = Invoice.id, back_populates = "customer")
#Base.metadata.create_all(engine)

#added:
def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'test_diagram.png')
    print("Success! Check the test_diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
