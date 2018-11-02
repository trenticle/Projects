import random

heads = 0
tails = 1

for i in range (1, 1001):
    if random.randint(0,1) == 1:
        tails = tails + 1
    else: 
        heads = heads + 1
                    
    if i == 499:
        print ('Halfway done!')
        print ('Heads came up ' + str(heads) + ' times.' + 'And, tails came up ' + str(tails) + ' times.')

    if i == 999:
        print ('Finished!')
        print ('Heads came up ' + str(heads) + ' times.' + 'And, tails came up ' + str(tails) + ' times.')


