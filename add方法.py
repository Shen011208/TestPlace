class Person:
    def __init__(self,name):
        self.name=name
    def __add__(other,another):
        return other.name+another.name

student1=Person("传道")
student2=Person("沈")

s=student2+student1
print(s)
print(student1.__dict__)
print(student2.__dict__)
print("***************************")
s2=student1.__add__(student2)
print(s2)
