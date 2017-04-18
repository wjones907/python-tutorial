# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

class MyClass1:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then pring out both values
print(myobjectx.variable)
print(myobjecty.variable)


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()

car1.color = 'red'
car1.name = 'Fer'
car1.value = 60000.00
car1.kind = 'convertible'

car2.color = 'blue'
car2.name = 'Jump'
car2.value = 10000.00
car2.kind = 'van'

# test code
print(car1.description())
print(car2.description())





