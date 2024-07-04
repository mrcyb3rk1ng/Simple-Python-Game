import os
import random
import time
def main():
	get_number = int(input(" Enter your number (1-5) : "))
	selected_number = random.randint(1,5)
	if get_number == selected_number:
		print("you have won! ")
		time.sleep(2)
		os.system('clear')
		main()
	else:
		print("you have lost!")
		print("The number was : ", selected_number)
		time.sleep(2)
		os.system('clear')
		main()
main()