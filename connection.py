from sqlalchemy import create_engine, Column, String, Text, ForeignKey, Integer
from sqlalchemy.orm import sessionmaker, declarative_base,relationship
from uuid import uuid4
from dotenv import load_dotenv
import os


load_dotenv()

connection_str = os.environ.get("DATABASE_URL")
engine = create_engine(connection_str, pool_pre_ping=True)


try:
    with engine.connect() as connection:
        print("Successfully connected to the database")
        connection.close()
except Exception as e:
    print(f"Failed to connect to database {e}")
    

session = sessionmaker(bind=engine)
db_session = session()


Base = declarative_base()

def generate_uuid():
    return str(uuid4())
     
class Students(Base):
    __tablename__ = "students"
    id = Column(String(60), primary_key= True, default=generate_uuid())
    email = Column(String(50), unique=True)
    age = Column(Integer(), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(60), nullable=False)
#for synchronization purposes.  
laptops = relationship("Laptop", back_populates= "students")

class Laptop(Base):
    __tablename__ = "laptop"
    laptop_id = Column(String(60), primary_key=True)
    laptop_name = Column(String(60), nullable=False)
    cpu = Column(String(30),nullable = False )
    version= Column(Integer(), nullable=False)
    students_id = Column(String(30), ForeignKey ('students.id'), nullable=False)

Students = relationship("Students", back_populates = "laptops")

#create tables in a database if they do not exists
Base.metadata.create_all(engine)
