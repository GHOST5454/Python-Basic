# Lets learn about Inheretance.

class Parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print(self.firstname+self.lastname)


class Child(Parent):
    pass


x = Parent("Sachin", "Ghunawat")
print(x)
