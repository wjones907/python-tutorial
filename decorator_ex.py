#
#
#Higher-order function
#In mathematics and computer science, a higher-order function (also functional, functional form or functor) is a function that does at least one of the following:
# takes one or more functions as arguments (i.e., procedural parameters),
# returns a function as its result

# All other functions are first-order functions. In mathematics higher-order functions are also termed operators or functionals. The differential operator in calculus is a common example, since it maps a function to its derivative, also a function.
#
# In the untyped lambda calculus, all functions are higher-order; in a typed lambda calculus, from which most functional programming languages are derived, higher-order functions that take one function as argument are values with types of the form {\displaystyle (\tau _{1}\to \tau _{2})\to \tau _{3}} (\tau _{1}\to \tau _{2})\to \tau _{3}.
#
#In the following examples, the higher-order function twice takes a function, and applies the function to some value twice. If twice has to be applied several times for the same f it preferably should return a function rather than a value. This is in line with the "don't repeat yourself" principle.

def twice(f):
    return lambda x: f(f(x))

def f(x):
    return x + 3

g = twice(f)

print g(7)

# result should be 13
