from sqlalchemy import Column,  Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from utils.uuid_generator import generate_uuid
"""from utils.connection import db_session"""
from models.laptop_model import Laptop




class Students(Base):
    __tablename__ = "students"
    id = Column(String(60), primary_key=True, default=generate_uuid())
    email = Column(String(50), unique=True)
    age = Column(Integer(), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(60), nullable=False)


# for synchronization purposes.
    laptops = relationship("Laptop", back_populates="Students")
    

