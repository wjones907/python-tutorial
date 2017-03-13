# Loops and Conditionals


def testWhileLoop():
    # While Loop
    a = 0
    while a < 10:
        a = a + 1
        print(a)

# Boolean Operators
# Table 1 - Boolean operators
# Expression	Function
# <	less than
# <=	less than or equal to
# >	greater than
# >=	greater than or equal to
# !=	not equal to
# <>	not equal to (alternate, != preferred)
# ==	equal to    

def testIfStatement():
    # Conditional Statement
    '''
    if {conditions to be met}:
        {do this}
        {and this}
        {and this}
    {but this happens regardless}
    {because it isn't indented}
    '''

    #EXAMPLE 1
    y = 1
    if y == 1:
        print ("y still equals 1, I was just checking")

    #EXAMPLE 2
    print ("We will show the even numbers up to 20")
    n = 1
    while n <= 20:
        n = n + 1
        if n % 2 == 0:
               print(n)
    print("there, done.")


def testIfandElif():
    #  the complete if syntax
    '''
    if {conditions}:
        {run this code}
    elif {conditions}:
        {run this code}
    elif {conditions}:
        {run this code}
    else:
        {run this code}

    #You can have as many or as few elif statements as you need
    #anywhere from zero to the sky.
    #You can have at most one else statement
    #and only after all other ifs and elifs.
    '''

    # If-Else Statement
    a = 1
    if a > 5:
        print("This shouldn't happen.")
    else:
        print("This should happen.")

    # Elif Statement

    z = 4
    if z > 70:
        print("Something is very wrong")
    elif z < 7:
        print("This is normal")

def testDoubleCondition():
    x=1
    y=3
    if x==1 and y==2:
        print 'x=1 and y=2'
    else:
        print 'either x!=1 or y!=2'
    print 'x=',x , 'y=',y


def testIndentation():
    # Indention
    '''
        - One other point is that the code to be executed if the conditions are met, MUST BE INDENTED
        - hat means that if you want to loop the next five lines with a 'while' loop, you must put a set number of spaces at the beginning of each of the next five lines.
    '''
    a = 10
    while a > 0:
        print(a)
        if a > 5:
            print("Big number!")
        elif a % 2 != 0:
            print("This is an odd number")
            print("It isn't greater than five, either")
        else:
            print("this number isn't greater than 5")
            print("nor is it odd")
            print("feeling special?")
        a = a - 1
        print("we just made 'a' one less than what it was!")
        print("and unless a is not greater than 0, we'll do the loop again.")
    print("well, it seems as if 'a' is now no bigger than 0!")
    print("the loop is now over, and without furthur ado, so is this program!")


def forloopex():
    i=range(10)
    print i


testDoubleCondition()
