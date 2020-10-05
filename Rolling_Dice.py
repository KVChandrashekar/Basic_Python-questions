import random
min = 1
max = 6

rollSecond = "yes"

while rollSecond == "yes" or rollSecond == "y":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))

    rollSecond = raw_input("Roll the dices again?")
