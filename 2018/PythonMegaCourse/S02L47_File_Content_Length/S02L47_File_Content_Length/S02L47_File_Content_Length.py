fruitsTxt = open('c://users//trent//desktop//fruits.txt')
myFruits = fruitsTxt.read()
myFruits = myFruits.splitlines()
fruitsTxt.close


for eachFruit in myFruits:
    print(len(eachFruit))


fruitsTxt = open('c://users//trent//desktop//fruits.txt')
myFruits = fruitsTxt.readlines()
myFruits = [line.strip() for line in myFruits]
fruitsTxt.close

for eachFruit in myFruits:
    print(len(eachFruit))



