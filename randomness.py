import random

while True:
	n = input()
	if n=="n":
		x=random.randint(1,2)
		if x==1:
			print("H")
		else:
			print("T")
