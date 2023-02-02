import random
import math

def suffix(num):
	if 4 <= num <=20:
		return('th')
	elif num == 1 or num%10==1:
		return('st')
	elif num == 2 or num%10==2:
		return('nd')
	elif num == 3 or num%10==3:
		return('rd')
	else:
		return('th')


l_bound = int(input("Enter Lower Bound: "))
u_bound = int(input("Enter Upper Bound: "))

x = random.randint(l_bound, u_bound)
print("You have only ",round(math.log(u_bound - l_bound + 1, 2)),"chances to guess the integer!\n")

i = 0
while i < math.log(u_bound - l_bound+1, 2):
	i = i+1
	user_guess = int(input("Guess a number: "))

	if x==user_guess:
		print("Hooray! You guessed it  right in your",str(i)+suffix(i)+" try.")
		break
	elif x>user_guess:
		print("Your guess is too small.")
	elif x<user_guess:
		print("Your guess is too high.")

if i >= math.log(u_bound - l_bound + 1, 2):
	print("The Number is: ",x)
	print("Well Tried! Good Luck Next time.")
