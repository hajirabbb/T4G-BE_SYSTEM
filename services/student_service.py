from models.students_model import Students
from utils.connection import db_session

#pass in variable called session
class StudentsServices:
    def __init__(self,session= db_session):
        self.session = session
        
    
    def create_student(self, first_name, last_name, email, age) :
        new_student = Students(first_name = first_name, last_name = last_name, email= email, age= age) 
        self.session.add(new_student)
        self.session.commit()
        return new_student

    def get_one_student(self, student_id):
        return self.session.query(Students).filter(Students.id == student_id).first()

    def get_all_students(self):
        all_students = self.session.query(Students).all()
        return all_students
       
            
    def update_student (self,student_id, first_name = None, last_name = None, age = None,email = None, ):
        found_student  = self.get_one_student(student_id)
        if not found_student:
            print("Student was not found")
        if found_student:
            found_student.first_name = first_name
        if found_student:
            found_student.last_name = last_name
        if found_student:
            found_student.age = age
        if found_student:
            found_student.email = email
        self.session.commit()
        return found_student
    
    def delete_student (self,student_id):
      found_student  = self.get_one_student(student_id)
      if found_student:
          self.session.delete(found_student)
          self.session.commit()   
