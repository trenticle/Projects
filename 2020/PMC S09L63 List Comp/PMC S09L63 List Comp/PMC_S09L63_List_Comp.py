#temps = [221, 234, 340, 320]

#create a new list (new_temps)
#new_temps = []
#for temp in temps:
#    new_temps.append(temp / 10)

#print(new_temps)
# old way above
# new way below

#new_temps = [temp / 10 for temp in temps]

# print(new_temps)
# confusing since variable "temp" is not defined. but saying "for temp in temps" is defining it.
# eliminates the need for "for" loops 

# L64 "if" conditional
# ignore null value

temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)

# exercise(its not correct)
#foo = ([99, 'no data', 95, 94, 'no data'])
#def foo(lst):
 #   return(i for i in lst if not isinstance(i, str))
#print()

# exercise
#foo([-5,3,-1,101])
#def foo(lst):
#    return[i for i in lst if i > 0]


temps = [221, 234, 340, -9999, 230]

# 'for' goes at the end when you have an "if-else" statement
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)

foo([99, 'no data', 95, 94, 'no data'])
def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst]

# exercise
foo(['1.2', '2.6', '3.3'])
def foo(lst):
    return sum([float(i) for i in lst])



