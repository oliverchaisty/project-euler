def fib(num1, num2, sum_of_evens):
	num3 = num1 + num2
	if num3 > 4000000:
		return sum_of_evens
	if num3 % 2 == 0:
		sum_of_evens += num3
	return fib(num2, num3, sum_of_evens)
print(fib(1, 1, 0))
