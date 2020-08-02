from pathlib import Path

myfile = open('d:\\users\\trent\\desktop\\sandbox\\fruits.txt')
content = myfile.read()
print(content)
print(content)

#close file
myfile.close()

#open and close
with open('d:\\users\\trent\\desktop\\sandbox\\fruits.txt') as myfile:
    content = myfile.read()
print(content)

#Path library opens AND closes the file
myfile = Path('d:\\users\\trent\\desktop\\sandbox\\fruits.txt')
print(myfile.read_text())

#write to mode='w'
with open('d:\\users\\trent\\desktop\\sandbox\\vegatables.txt', 'w') as myOtherFile:
    myOtherFile.write("Tomato \nCucumber \nOnion")

#exercises
def foo(character, filepath='bear.txt'):
    file = open(filepath)
    content = file.read()
    return content.count(character)

with open('file.txt', 'w') as file:
    file.write('snail')
    file.close()

#note: "file.read" means same thing as "copy"
with open('bear.txt') as file:
    content = file.read()
with open('first.txt','w') as file:
    file.write(content[:90])

#reset cursor to top of text file:
#this way printing of all text below the cursor can be done
myfile.seek(0)

#2nd exercises
with open ('bear1.txt') as file:
    content = file.read()
with open ('bear2.txt', 'a+') as file:
    file.write(content)

with open('data.txt', 'a+') as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)

