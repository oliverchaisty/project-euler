number = 999999
def find(number):
	for i in range (1, 1000000):
		number -= 1
		string = str(number)
		if string[0] == string[5] and string[1] == string[4] and string[2] == string[3]:
			for j in range (999, 899, -1):
				for k in range(999, 899, -1):
					if j*k == number:
						return(number)
print(find(number))
