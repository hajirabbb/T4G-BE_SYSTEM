from sqlalchemy import Column,  Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from utils.uuid_generator import generate_uuid
"""from utils.connection import db_session"""





class Students(Base):
    __tablename__ = "students"
    id = Column(String(60), primary_key=True, default=generate_uuid())
    email = Column(String(50), unique=True)
    age = Column(Integer(), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(60), nullable=False)


# for synchronization purposes.
    laptops = relationship("Laptop", back_populates="Students")


def __str__(self):
    return f"Id: {self.student.id}, First_name: {self.student.first_name}, Last_name: {self.student.last_name}, Email: {self.student.email}"

    

