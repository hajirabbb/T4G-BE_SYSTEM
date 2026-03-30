from models.laptop_model import Laptop
from models.students_model import Students
from utils.connection import db_session

# pass in variable called session


class LaptopServices:
    def __init__(self, session=db_session):
        self.session = session

    def create_laptop(self, laptop_name, cpu, version, students_id):
        new_laptop = Laptop(laptop_name=laptop_name,
                               cpu=cpu, version=version, students_id=students_id)
        self.session.add(new_laptop)
        self.session.commit()
        return new_laptop

    def get_all_laptop(self):
        all_laptop = self.session.query(Laptop).all()
        for laptop in all_laptop:
            print(
                f"Id: {laptop.laptop_id}, laptop_name: {laptop.laptop_name}, cpu: {laptop.cpu}, version: {laptop.version}student_id:{laptop.students_id}")

    def update_laptop(self, laptop_id, laptop_name=None, cpu=None, students_id=None, version=None):
        found_laptop = self.get_one_laptop(laptop_id)
        if not found_laptop:
            print("laptop was not found")
        if found_laptop:
            found_laptop.laptop_name = laptop_name
        if found_laptop:
            found_laptop.cpu = cpu
        if found_laptop:
            found_laptop.students_id = students_id
        if found_laptop:
            found_laptop.version = version
        self.session.commit()
        return found_laptop

    def delete_laptop(self, laptop_id):
        found_laptop = self.get_one_laptop(laptop_id)
        if found_laptop:
            self.session.delete(found_laptop)
            self.session.commit()
