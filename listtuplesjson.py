# for making a tuple

MyTuple = (89,32)
MyTupleWithMoreValues = (1,2,3,4,5,6)

# To concatenate tuples
AnotherTuple = MyTuple + MyTupleWithMoreValues
print AnotherTuple

# it should print 89,32,1,2,3,4,5,6

# To get Value from tuple
firstVal = MyTuple[0]
secondVal = MyTuple[1]
print 'firstVal:',firstVal
print 'secondVal:',secondVal

# usage is more like a list

# if you got a function that returns a tuple than you might do this
Tup = (1,2)
Tup2 = (3,4,5)
Tup3 = [{"x":"1","y":"2","z":"3"}]
x=Tup()[0]  # x=1
y=Tup()[1]  # y=4

#or This
v1,v2 = Tup()

def tup():
    return (2,"hello")

i = 5 + tup()[0]
#return first element


