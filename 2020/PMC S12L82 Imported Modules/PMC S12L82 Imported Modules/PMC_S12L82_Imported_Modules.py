import sys
import time
import os
import pandas

#while True: 
#    if os.path.exists('d:\\Users\\trent\\Desktop\\Sandbox\\vegatables.txt'):
#        with open('d:\\Users\\trent\\Desktop\\Sandbox\\vegatables1.txt') as file:
#            print(file.read())
#    else:
#        print('the file does not exist')
#    time.sleep(10)

#os.path.exists('d:\\Users\\trent\\Desktop\\Sandbox\\vegatables.txt')

while True: 
    if os.path.exists('d:\\Users\\trent\\Desktop\\Sandbox\\temps_today.csv'):
        data = pandas.read_csv('d:\\Users\\trent\\Desktop\\Sandbox\\temps_today.csv')
        print(data.mean())
    else:
        print('the file does not exist')
    time.sleep(10)





