import random
from time import sleep


def LoopTries(stay):
	success = 0
	for i in range(1001):
		print("\tCompleted: " + str(i) + "/1000", end="\r")
		success += Try(stay)
	print("\b\n\tSuccess rate: " + str(float(success)/10) + "%")

def Try(stay):
	sleep(0.001)
	doors = [0,0,1]
	random.shuffle(doors)
	chosen = doors[0]
	nextDoor = 0
	if doors[2] == 0:
		nextDoor = 1
	else:
		nextDoor = 2
	if stay:
		if chosen == 1:
			return 1
		else:
			return 0
	else:
		if doors[nextDoor] == 1:
			return 1
		else:
			return 0

print("Welcome to the Monty Hall test program!\n")
print("Your chances if you stay:")
LoopTries(True)
print("Your chances if you change your decision:")
LoopTries(False)