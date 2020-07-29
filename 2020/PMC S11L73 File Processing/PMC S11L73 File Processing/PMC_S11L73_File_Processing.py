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

