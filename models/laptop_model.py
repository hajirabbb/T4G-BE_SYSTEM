from sqlalchemy import Column,  Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base 
from utils.uuid_generator import generate_uuid

class Laptop(Base):
    __tablename__ = "laptop"
    laptop_id = Column(String(36), primary_key=True, default=generate_uuid())
    laptop_name = Column(String(60), nullable=False)
    cpu = Column(String(30), nullable=False)
    version = Column(Integer(), nullable=False)
    students_id = Column(String(36), ForeignKey('students.id'), nullable=False)


# backpopulates is for synchroniztion purposes
    Students = relationship("Students", back_populates="laptops")


# create tables in a database if they do not exists

def __str__(self):
    return f"Id: {self.laptop.laptop_id}, laptop_name: {self.laptop.laptop_name}, cpu: {self.laptop.cpu}, version: {self.laptop.version}student_id:{self.laptop.students_id}"

