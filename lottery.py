import random

''' Lottery game that lets user pick 5 numbers plus powerball number to see if they won. 
If user loses the program will print out the winning numbers anyway. If user enters more than 5 numbers or more
than 1 power ball number, the program will ask user to try again and choose 5 numbers.
'''

lottery = random.sample(range(1, 64),5) #create variable that will output random lottery numbers from 1-64
powerball = random.randint(1, 21) #create the last powerball variable that selects random number from 1-21

lotto_pick = input("Select 5 numbers from 1 to 64: ").split(",")
powerball_selection = input('Enter powerball number: ')

if lotto_pick and powerball_selection == lottery and powerball:
    print("You have won the powerball Lottery!!!")
elif powerball_selection == powerball:
    print("Your powerball number matches!!")
elif len(lotto_pick) > len(lottery) or len(lotto_pick) < len(lottery):
    print("Try again, please choose 5 numbers")
else:
    print("Sorry the lottery numbers are:" , lottery)
    print("And the powerball number is " , powerball)

