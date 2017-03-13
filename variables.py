"""
    Variables in Python
"""



# Variables demonstrated
def variables_demonstrated():
    print ("This program is a demo of variables.")
    v = 1
    print("The value of v is now", v)
    v = v + 1
    print("v now equals itself plus one, making it worth", v)
    v = 51
    print("v can store any numerical value, to be used elsewhere.")
    print("For example, in a sentence. v is now worth", v)
    print("v times 5 equals", v * 5)
    print("But v still only remains", v)
    print("To make v five times bigger, you would have to type v = v * 5")
    v = v * 5
    print("There you go, now v equals", v, "and not", v / 5)


    #Giving variables text, and adding text.
    word1 = "Good"
    word2 = "morning"
    word3 = "to you too!"
    print(word1, word2)
    sentence = word1 + " " + word2 + " " + word3
    print(sentence)

    #Strings
    #Giving variables text, and adding text.

    word1 = "Good"

    word2 = "morning"

    word3 = "to you too!"
    print(word1, word2)

    sentence = word1 + " " + word2 + " " + word3

    print(sentence)

# Variable Scope
def variable_scope():
    # This is a global variable
    a = 0

    if a == 0:
        # This is still a global variable
        b = 1

    def my_function(c):
        # this is a local variable
        d = 3
        print(c)
        print(d)

    # Now we call the function, passing the value 7 as the first and only parameter
    my_function(7)

    # a and b still exist
    print(a)
    print(b)

    # c and d don't exist anymore -- these statements will give us name errors!
    print(c)
    print(d)

# Global / Local Variable example
# what value will be printed by both print(a) statements
def local_global_example():
    a = 0

    def my_function():
        a = 3
        print(a)

    my_function()

    print(a)

    # first print(a) will print 3
    # second print(a) will print 0
    # this is because any local variable name is created as local by default unless otherwise defined locally
    # what happens if i just print(a) in the first case - but do not assign a = 3?

def local_global_example2():
    a = 0

    def my_function():
        global a
        a = 3
        print(a)

    my_function()

    print(a)
    # now you get 3 printed in both statements since we used the global a statement
