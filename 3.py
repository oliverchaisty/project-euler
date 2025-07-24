array = []
def prime_factors(number, prime_numbers):
	for i in prime_numbers:
		if i > number:
			break
		if number % i == 0:
			return (i, prime_factors(number/i, prime_numbers))

def sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

prime_numbers = sieve(1000000)

array.append(prime_factors(600851475143, prime_numbers))
for i in array:
	print(i)
print(array)
