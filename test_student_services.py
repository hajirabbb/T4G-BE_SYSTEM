from services.student_service import StudentsServices

service = StudentsServices()

# Create
student = service.create_student(
    first_name="richard",
    last_name="Peter",
    email="akosua@example.com",
    age=20
)
print("Created:", student.id, student.first_name, student.email)

# Read all
print("\nAll students:")
service.get_all_students()

# Update
updated = service.update_student(
    student_id=student.id,
    first_name="Jane",
    last_name="Smith",
    email="jane@example.com",
    age=22
)
print("\nUpdated:", updated.id, updated.first_name, updated.email, updated.age)

# Delete
service.delete_student(student.id)
print("\nDeleted student.")

# Read all again
print("\nStudents after delete:")
service.get_all_students()
