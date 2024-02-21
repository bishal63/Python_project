#number guessing game
import random
randomnumber=random.randrange(1,300)
print(randomnumber)
userinput=int(input("guess the game:"))
if userinput > randomnumber:
    print(randomnumber)
    print("the number is too high")
elif userinput < randomnumber:
    print(randomnumber)
    print("the number is low")
else:
    print(randomnumber)
    print("yes,matched the number")