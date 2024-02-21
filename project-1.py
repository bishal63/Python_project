#number gueesing game
import random

randomnumber=random.randrange(1,200)
print(randomnumber)
userinput=int(input("guess the number:"))
if userinput > randomnumber:
    print(randomnumber)
    print("the number is to high")
elif randomnumber > userinput:
    print(randomnumber)
    print("the number is too low")
else:
    print(randomnumber)
    print("yes,you matched the number")


'''import random
randomnumber=random.randrange(1,200)
print(randomnumber)
userinput=int(input("guess the number:"))
if randomnumber > userinput:
    print(randomnumber)
    print("the number is too high")
elif userinput > randomnumber:
    print(randomnumber)
    print("the number is too low")
else:
    print(randomnumber)
    print("yes,you matched the number")'''

import random
randomnumber=random.randrange(1,100)
#print(randomnumber)
inputnumber=int(input("guess the number:"))
if randomnumber>inputnumber:
    print(randomnumber)
    print("the number is too high")
elif randomnumber<inputnumber:
    print(randomnumber)
    print("the number is too low")
else:
    print(randomnumber)
    print("matched the number")