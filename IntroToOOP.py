# class/blueprint
class School:
    # parameterized constructor
    def __init__(self, name):
        self.name = name            # -> instance variable
        # print(self)               # -> prints the memory location of that object which is always unique
        # print(f"{self.name} at {self}, 'created'")

# objects
st1 = School("Nazif")
st2 = School("Nogif")
#
# name = input("Enter your name: ")
# st3 = School(name)

print(st1.name)
print(st2.name)

st2.name = "Meowmeow"
print(f"Name: '{st2.name}' after change")