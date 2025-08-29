
student_db = {

	1: {'name': 'John', 'age': 13, 'department': 'comp'},
	2: {'name': 'Jane', 'age': 43, 'department': 'data'},
	3: {'name': 'Jane', 'age': 20, 'department': 'bch'}
}


def add_student():
	name = input("Enter your name>>> ")
	age = int(input("Enter your age>>> "))
	department = input("Enter your department>>> ")
	
	if not student_db:
		student_db.update({1: {'name': name, 'age': age, 'department': department}})
		print("Your student id number is 1")
	else:
		id_number = len(student_db) + 1
		student_db.update({id_number: {'name': name, 'age': age, 'department': department}})
		print(f"Your student id number is {id_number}")

def delete_student():
	student_id = int(input("Enter the id of the student you want to delete>>> "))
	if student_id in student_db.keys():
		del student_db[student_id]
		print(f'Student with id of {student_id} has been removed')
	else:
		print("Student not found")

	
def update_student():
	student_id = int(input("Enter the id of the student whose information you want to update>>> "))
	if student_id in student_db.keys():
		name = input("Enter name>>> ")
		age = input("Enter age>>> ")
		department = input("Enter department>>> ")
		student_db.update({student_id: {'name': name, 'age': age, 'department': department}})		
		print(f'''
Student with id no {student_id} updated succesfully 
{student_db[student_id]}
		''')

	else:
		print(f"Student with id {student_id} not found") 

def display_one_student():
	student_id = int(input("Enter student id>>> "))
	if student_id in student_db.keys():
		print(student_db[student_id])
	else:
		print("Student not found")
	 
def display_all_students():
	for student in student_db.keys():
		print(student_db[student])

def search_student_by_name():
	name = input("Enter name>>> ")
	students_found = []
	for i in range(len(student_db.values())):
		if list(student_db.values())[i]['name'] == name:
			students_found.append({list(student_db.keys())[i] : list(student_db.values())[i]})
	if students_found:
		for student in students_found:
			print(student)
	else:
		print("Not found")

		
def count_students():
	print("The total number of students: ", len(student_db))		

def filter_by_age():
	age = int(input("Enter minimum age>>>"))
	students_found = []
	for i in range(len(student_db.values())):
		if list(student_db.values())[i]['age'] >= age:
			#students_found.append(list(student_db.items())[i])
				students_found.append({list(student_db.keys())[i]: list(student_db.values())[i]})

	if students_found:
		for student in students_found:
			print(student)
	else:
		print("Not found")	

def start():
	print( '''
STUDENT MANAGEMENT SYSTEM
`--------------------------
Available commands:
1 to Add Student
2 to Delete Student
3 to Update Student
4 to Display One Student
5 to Display All Students
6 to Search Student by Name
7 to Show the total number of students in the system
8 to Filter by age
9 to Terminate the program
	''')
	execute = True
	while execute:
		command = input("Enter command>>> ")
		if command == '1':
			add_student()	
		elif command == '2':
			delete_student() 
		elif command == '3':
			update_student()
		elif command == '4':
			display_one_student()
		elif command == '5':
			display_all_students()
		elif command == '6':
			search_student_by_name()
		elif command == '7':
			count_students()	
		elif command == '8':
			filter_by_age()
		elif command == '9':
			execute = False
		else:
			print("Invalid command") 

start() 
