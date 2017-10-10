class Students:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def accept_data(self):
        print("Accepting Data")
        self.name = input("Enter name : ")
        self.contact = input("Enter contact num : ")

    def print_data(self):
        print("Name is "+self.name , "and Contact is "+self.contact)


Joel = Students(None,None)
Joel.accept_data()
Joel.print_data()