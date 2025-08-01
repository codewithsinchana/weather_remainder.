class employee():
    def __init__(self,role,department,salary):
     self.role = role 
     self.department = department
     self.salary = salary
     def showdetails(self):
         print("Role:", self.role)
         print("Department:", self.department)
         print("Salary:", self.salary)
e1 = employee("Software Engineer", "IT", 60000)
e2 = employee("Data Scientist", "Analytics", 70000)
print(e1.role, e1.department, e1.salary)
print(e2.role, e2.department, e2.salary)
e1.showdetails()
e2.showdetails()
print("Employee 1 Details:")

