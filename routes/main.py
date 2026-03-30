from fastapi import FastAPI, status , HTTPException, Body
from fastapi.encoders import jsonable_encoder
from services.student_service import StudentsServices
from services.laptop_service import LaptopServices

student_service = StudentsServices()
laptop_service = LaptopServices
#calling an instance of the class
app = FastAPI()
#to use the instance, use the decorator @
#specify the root. if anyone requires a service they specify a route

@app.get('/')
def home():
    return {"message ": "Welcome to FastAPI"}




@app.get('/students', status_code=status.HTTP_200_OK)
def fetch_students():
    student_fetched = student_service.get_all_students()
    if not student_fetched:
        raise HTTPException(status_code=404, detail="No students found")
    return jsonable_encoder(student_fetched)


app.get('/laptops',status_code=status.HTTP_200_OK )
def fetch_laptops():
    pass


#request body would always be required ...
#body is a dictionary use .get to get values of the dictionary
@app.post('/students',status_code=status.HTTP_201_CREATED)
def create_student(body: dict = Body(...)):
    new_student = student_service.create_student(
        first_name=body.get("first_name"),
        last_name=body.get("last_name"),
        email=body.get("email"),
        age=body.get("age")
       
        )
    return jsonable_encoder(new_student)
    
    
    
    
     
   
       
   


