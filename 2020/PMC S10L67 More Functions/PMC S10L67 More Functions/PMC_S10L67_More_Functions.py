#def area (a, b):
    #return a*b
#print(area(4, 5))

# shit exercise not well defined, how can you print this garbage? return s1 + s2, no space? crap! yeah, checks out, it's pure garbage.
#def foo(s1, s2):
    #return s1 + s2
#s1 = "me"
#s2 = "too"

#print(foo(s1, s2))

# 2 kinds of arguements: keyword and non-keyword arguements
 #default perameters (b=6) in definition
# non-default (variable) must go first in list before default(fixed value) perameters

#def mean(*args):
    #return sum(args) / len(args)

#print(mean(1, 4, x=3))

#exercise
#wrong answer
foo = (10, 20, 30, 40)
#def mean(*foo):
    #return sum(foo) / len(foo)
#print(mean(foo))

#right answer
#def foo(*args):
    #return sum(args) / len(args)
#print(foo())

#def foo(*args):
    #args = [x.upper() for x in args]
    #return sorted(args)

#def mean(**kwargs):
    #return kwargs
#print (mean(a=1, b=2, c=3))

def find_sum(**kwargs):
    return sum(kwargs.values())
print(find_sum(x=9))



