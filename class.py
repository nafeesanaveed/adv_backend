class Student:

    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("CGPA:", self.cgpa)

    def check_result(self):
        if self.cgpa >= 2.0:
            print("Passed")
        else:
            print("Failed")


student1 = Student("Nafeesa", 23, 3.65)

student1.display()
student1.check_result()