class Person:
    def __new__(cls, p, q):
        print('cls的id值为:{}'.format(id(cls)))
        id1 = object.__new__(object)
        print(id1)
        print('创建的对象的id值为{}'.format(id(id1)))
        return id1


def __init__(self, name, age):
    print('self的id值为{}'.format(id(self)))
    print("***********")
    self.name = name
    self.age = age
    print('他的名字{},他的年龄{}'.format(self.name, self.age))


print('object这个类对象的id为{}'.format(id(object)))
print('Person这个类对象的id为{}'.format(id(Person)))

p1 = Person("沈传道", 25)
p2 = Person("沈传达", 78)
print("_______________--------------")
print('p1的id值为{}'.format(id(p1)))
print('p2的id为{}'.format(id(p2)))
