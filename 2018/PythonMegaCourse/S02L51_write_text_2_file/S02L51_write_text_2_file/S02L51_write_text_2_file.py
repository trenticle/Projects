# file = open('c://users//trent//desktop//newtext.txt', 'x')
# file.close

file = open('c://users//trent//desktop//newtext.txt', 'w')
numbers = ['one', '2', '3']
for i in numbers:
    file.write((i) + '\n')
file.close()



