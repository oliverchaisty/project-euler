flag = False
counter=20
while flag == False:
	counter += 20
	flag = True
	for i in range (1,21):
		answer = counter%i
		if answer != 0:
			flag = False
			print(counter)
			break
print(counter)
