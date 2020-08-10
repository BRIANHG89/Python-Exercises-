
#reading a file in python 

employee_file = open("employees.txt", "r")

for employee in employee_file.read_lines():
    print(employee)

employee_file.close()


