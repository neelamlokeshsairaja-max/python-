'''
 built in function:
 ===============[
math functions
celi : round up
floor : round down'''
'''
import math
print(math.pi)
print(math.ceil(4.3))
print(math.sqrt(25))
print(math.sin(3))
print(math.pow(2,3))
print(math.cos(5))
'''

      

'''import random
print(random.randint(1,100))
print(random.randint(2,200))

color = ['red','blue','green','yellow','orange']
print(random.choics(color))
random.shuffle(color)
print(color)
'''

'''import platform
print(platform.python_version())
print(platform.system())
print(platform.platform())
print(platform.processor())
'''



'''import collections
data = ['banana','apple','banana','orange','orange']
print(collections.counter(data))
all = collections.counter(data)
print(all most common())'''



'''from collections import defaultdict
data_ = defaultdict(list)
data_['python'].append('raj')
data_['python'].append('hhh')
print(data_)'''


'''date and time:
==============    =

from datetime import datetime
today = datetime.today()
now = datetime.now()
print(today.month)
print(today.day)
print(today.year)
print(today.hour)
print(today.minute)
'''



'''from datetime import datetime
now = datetime.now()
print(now.strftime('%d-%m-%y'))
print(now.strftime('%h-%m-%s'))
'''

'''
import random

num = random.randint(10, 100)
print(num)

'''


'''import random
attep = 3
num = random.randrange(start:1,stop:100)
print(num)
while attep > 0:
    game = int(input('enter a number between 1 and 100: '))
    if game == num:
        print('your guess is corect')
        break
    else:
        attep = 1'''


'''

import random

attep = 3
num = random.randint(1, 100)

while attep > 0:
    game = int(input("Enter a number between 1 and 100: "))

    if game == num:
        print("Your guess is correct!")
        break
    else:
        attep -= 1
'''



'''import random

attep = 3
num = random.randint(1, 100)
prize = 1000

while attep > 0:
    game = int(input("Enter a number between 1 and 100: "))

    if game == num:
        print("Your guess is correct!")
        print("You won ₹", prize)
        break
    else:
        attep -= 1
        print("Wrong guess!")
        print("Attempts left:", attep)

if attep == 0:
    print("Game over!")
    print("The number was:", num)
'''

'''
import itertools
a = itertools.count(45)
print(next(a))
print(next(a))
b = itertools.repeat('python',6)
for j in b:
      print(j)

c = itertools.cycle(['Python','java','C'])
print(next(c))
'''


import intertools
n =  intertools.chain(iterables[1,2,3],[4,5,6])
print(list(n))











