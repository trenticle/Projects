myList = [1, 2, 3, 4, 5]
for allNumbers in myList:
    print(allNumbers)

for i in (1, 2, 3):
    print(i + 1)

a = 'tricky'
for i in a[:3]:
    print (i)

myNewList = ['more tricky']
for item in myNewList:
    print (item)

myOtherList = ['terribly tricky']
for word in myOtherList:
    for letter in word[-6:]:
        print(letter)

anotherList = [1, 2, 3, 4, 5]
for lastThreeNumbers in anotherList[2:]:
    print(lastThreeNumbers)

stillAnotherList = [1, 2, 3, 4, 5]
for someNumbers in stillAnotherList:
    if someNumbers > 2: 
        print(someNumbers)

