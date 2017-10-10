class Student:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        print("Init of Parent")

    def accept_data(self):
        print("Accepting Data")
        self.name = input("Enter name : ")
        self.contact = input("Enter contact num : ")

    def print_data(self):
        print("Name is "+self.name , "and Contact is "+self.contact)


class ScienceStudent(Student):

    def __init__(self,age):
        self.age = age
        print("Init of child")

    def science(self):
        print("I am a science student")


johnny = ScienceStudent(29)
johnny.accept_data()
johnny.print_data()
johnny.science()
