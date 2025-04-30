
class Employee:
    def __init__(self,name,age,salary,gender):  # init method acts as the constructor
                                                # in the init two underscore is must

        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

    def employee_details(self):
        print("Name of the Employee",self.name)
        print("Age of the Employee",self.age)
        print("Salary of the Employee",self.salary)
        print("gender of the Employee",self.gender)

e1=Employee('sam',45,45000,'male')
e1.employee_details()