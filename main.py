class Plants:
    def about(self):
        height =

class Parent(Grandparent):
    def about_myself(self):
        print("I am Parent")

class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()

pp = Parent()
pp.about_myself()

nick = Child()
nick.about_myself()
nick.about()



class DollHouse:
    def __init__(self):
        super().__init__()
        self.height = 128
        self.color = "pink"
        self.age = 1
        self.material = "plastic"

class Doll(DollHouse):
    def __init__(self):
        super().__init__()
        self.material = "wood"
        self.dress = 1

class Human:
    height=170
    satiety=50
class Student(Human):
    satiety=0

class Worker(Human):
    satiety=100

nick = Student()
ann = Worker()
print(nick.satiety)
print(ann.satiety)

super().about()
super().about_myself