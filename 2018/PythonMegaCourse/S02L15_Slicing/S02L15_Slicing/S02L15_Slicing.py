address = ['Flat Floor Street', '18', 'New York']
pins = {'Mike':1234, 'Joe':1111, 'Jack':2222}

print(address[0], address[1])

pin = int(input('Enter your pin: '))

def find_in_file(f):
    myFile = open('c://users//trent//desktop//test1.txt')
    fruits = myFile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return 'That fruit is not on the list.'
    else:
        return 'No such fruit found!'

if pin in pins.values():
    fruit = input('Enter fruit: ')
    print(find_in_file(fruit))
else:
    print('Incorrect pin!')
    print('This info can only be accessed by: ')
    for key in pins.keys():
        print(key)
