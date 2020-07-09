def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean
student_grades = {"Mary":4.0, "Sim":3.89, "John":3.1}
print(mean(student_grades))

def foo(pw):
    if len(pw) > 4:
        return("suck it")
    else:
        return("fuck it")
pw = "eat shit"
print(foo(pw))

def bar(temp):
    if temp > 98.6:
        return("you gonna die")
    elif temp >=90.0 <=98.5:
        return("please leave hypochondriac")
    else:
        return("you dead")
temp = 89.9
print(bar(temp))

def foobar(tempx):
    if tempx > 88.0:
        return("HOT!")
    elif tempx >= 40.0 <= 87.9:
        return ("Warm")
    else:
        return("Cacacacold")
tempx = 300.0
print(foobar(tempx)) 

def weather_condition(temperature):
    if temperature > 7:
        return ("Warm")
    else:
        return ("Cold")
user_input = float(input("Enter temperature:"))
print(weather_condition(user_input))