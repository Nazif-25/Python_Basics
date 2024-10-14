class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print(f"{self.name} and {self.id} has been registered at {self}")

    def compare(self, ct):
        if self.id == ct.id:
            print("They are the same")
        else:
            print("They are not the same")

# default init constructor can only be called once but methods can be called 'n' times
s1 = Student("Nazif", 6789)
s2 = Student("Nadfdfzif", 6785459)

# the following two give the same result
print(s1.details())
s1.details()

print(s1.details)

s1.compare(s2)
