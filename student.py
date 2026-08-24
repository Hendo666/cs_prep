class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

student1 = Student("Euan", 26)
student2 = Student("Sarah", 25)

student1.say_hi()
student2.say_hi()