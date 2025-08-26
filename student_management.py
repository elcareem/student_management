
student_db = {
}


def add_student():
	name = input("Enter your name>>> ")
	age = input("Enter your age>>> ")
	department = input("Enter your department>>> ")
	
	if not student_db:
		student_db.update({1: {'name': name, 'age': age, 'department': department}})
		print("Your student id number is 1")
	else:
		id_number = len(student_db) + 1
		student_db.update({id_number: {'name': name, 'age': age, 'department': department}})
		print(f"Your student id number is {id_number}  ")
def delete_student():
	student_id = "Enter the id of the student you want to delete>>>"
	removed_id = student_db.pop(student_id, 'Not found')
	print(f'Student with id of {removed_id} has been removed')
	
def update_student():
	student
def start():
	display_info = '''
STUDENT MANAGEMENT SYSTEM
--------------------------
Enter commands:
1 to Add Student
2 to Delete Student
3 to Update Student
4 to Display One Student
5 to Display All Students

'''

	command = input(display_info)

	while True:
		if command == 1:
			pass
		elif command == 2:
			pass 
		elif command == 3:
			pass
		elif command == 4:
			pass
		elif command == 5:
			pass 
		elif command == 6: 
			pass
		elif command == 7:
			pass
		else:
			"Invalid command" 

  
