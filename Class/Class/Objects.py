# Know Lets learn about classes and objects.

class First:
    print("Hello World!")


P1 = First()
print(P1)

# Class with Function.
class Second:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
        print("Hello i am "+self.Name+", I am "+str(self.Age)+" Old.")


P2 = Second("Sachin", 21)
print(P2)
