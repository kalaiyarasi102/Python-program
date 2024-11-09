class employee:
 def_init_(self id,name,salary,department):
   self.name=name:
   self.id=id:
   self.salary=salary:
   self.department=department:
 def show_details(self):
   print("name:{self.name}")
   print("department:{self.department})
   print("salary:{self.salary})
         
 def get_salary(self):
    return self_salary
 def get_department(self):
    return self_department

emp=employee(1,"kalai",80000,"HR")
   emp.show_details()
print("salary:",emp.get_salary())
print("department:",emp.get_department())
