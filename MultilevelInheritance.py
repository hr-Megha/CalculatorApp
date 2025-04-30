# In Multilevel Inheritance we have Parent, child and grandchild relationship

class Parent():
    def assign_name(self,name):
        self.name=name
    
    def show_name(self):
        return self.name

class child(Parent):
    def assign_age(self,age):
        self.age=age
    
    def show_age(self):
        return self.age
    
class grandChild(child):
    def assign_gender(self,gender):
        self.gender=gender
    
    def show_gender(self):
        return self.gender
    

gch=grandChild()

gch.assign_name("Megha")
gch.assign_age(45)
gch.assign_gender('Female')

print(gch.show_age())
print(gch.show_gender())
print(gch.show_name())
        