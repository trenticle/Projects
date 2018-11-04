correctPassword = '1234'
userName = input('Enter name!!')
password = input('Enter Password! ')
while correctPassword != password:
    password = input('Wrong password, enter again! ')

print('Hi %s you are logged in.' % userName)

import os
os.listdir()
