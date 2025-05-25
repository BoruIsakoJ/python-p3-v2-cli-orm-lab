from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the denamepartment's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")

def find_employee_by_id():
    id = int(input("Enter employee's id: "))
    employee = Employee.find_by_id(id)
    if employee:
        print(employee)
    else:
        print(f"Employee {id} not found")



def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = int(input("Enter the employee's department id:"))
    
    departments = Department.get_all()
    departments_id_array = []
    for dep in departments:
        departments_id_array.append(dep.id)
    
    if type(name)!=str: #I tried to use invalid data(like 2 for name) but it kept adding because the input will always return a string
        print("Name must be a non-empty string")
    
    elif type(job_title)!=str:
        print("Name must be a non-empty string")
        
    elif not (department_id in departments_id_array):
        print("department_id must reference a department in the database")
    
    
    try: 
        employee = Employee.create(name,job_title,department_id)
        print(f"Success: {employee}")
        
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    id = int(input("Enter the employee's id: "))
    if employee := Employee.find_by_id(id):
        try:
            name = input("Enter the employees's new name: ")
            employee.name = name
            job_title = input("Enter the employee's new job title: ")
            employee._job_title = job_title
            department_id = input("Enter the employees's new department id: ")
            employee._department_id = department_id
            
            employee.update()
            print(f"Success: {employee}")
        except Exception as exc:
            print(f"Error updating employee: {exc}")
    else:
        print(f"Employee {id} not found")

def delete_employee():
    id = int(input("Enter the employee's id: "))
    if employee := Employee.find_by_id(id):
        employee.delete()
        print(f"Employee {id} deleted")
    else:
        print(f"Employee {id} not found")       


def list_department_employees():
    id = int(input("Enter the department's id: "))
    if department := Department.find_by_id(id):
        employees = Employee.get_all()
        employees_with_id = []
        for employee in employees:
            if employee.department_id == id:
                print(employee)
    else:
        print(f"Department {id} not found")        