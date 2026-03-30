from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
from models.base import Base
from models.students_model import Students
from models.laptop_model import Laptop


load_dotenv()
#connection string is private
#dotenv purpose is to store database credentials
#inside.env, stuff are stored in key value pairs.
connection_str = os.environ.get("DATABASE_URL")
engine = create_engine(connection_str, pool_pre_ping=True)


try:
    with engine.connect() as connection:
        print("Successfully connected to the database")
        connection.close()
except Exception as e:
    print(f"Failed to connect to database {e}")
    




Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)
db_session = session()
"""yaa= Students(first_name="Ama", last_name="Baffoe",age=27, email="yaa@gmailcom")
db_session.commit()
db_session.add(yaa)
#READ ALL
all_students = db_session.query(Students).all()
for student in all_students:
    print(f"Id:{student.id} , First_name:{student.first_name}, last_name {student.last_name}, Email:{student.email}")
#REAd Criteria
hajira = db_session.query(Students).filter_by(
    email="hajira@gmailcom").first()
print(f" Id: {hajira.id}, First_name: {hajira.first_name}, last_name: {hajira.last_name},Email: {hajira.email}")


#UPDate

student_to_update = db_session.query(Students).filter_by(first_name ="hajira").first()
if student_to_update:
    student_to_update.age = 21
    student_to_update.email = "ama44@gmail.com"
    db_session.commit()
    print(f"Updated students details are {student_to_update.last_name} {student_to_update.age}, {student_to_update.email}")
else:
    print(f"student with name hajira not found ")
#Delete
student_to_delete = db_session.query(
    Students).filter_by(first_name="hajira").first()
if student_to_delete:
    db_session.delete(student_to_delete)
    db_session.commit()
    print(f"{student_to_delete.first_name} has been deleted successfully")
else:
    print(f"student was not found")"""
    
yaa = Students(first_name = "yaa", last_name ="Carson",email ="yaa@gmail.com", age = 25 )
db_session.add(yaa)
db_session.commit()
pamela_s_laptop = Laptop(laptop_name = "HP Elitebood", cpu ="intel core 17", version =22, students_id = yaa.id)
db_session.add(pamela_s_laptop)
db_session.commit()
print(f"New Addition Info Id: {yaa.id}, First_name: {yaa.first_name}, last_name: {yaa.last_name}, Email: {yaa.email}")
print(f"New Laptop Additon - Id:{pamela_s_laptop.laptop_id},Owner:{pamela_s_laptop.students_id} laptop_Name{pamela_s_laptop.laptop_name}")





