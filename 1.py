result = 0
multiples = []
for i in range(1000):
	if i % 3 == 0 or i % 5 == 0:
		multiples.append(i)
for i in multiples:
	result += i
print(multiples)
print(result)

# Notes to improve
# It would've been better if I used a single value and incremented it rather than adding each multiple to an array
# Next time I don't need to keep every value, I won't, I'll just increment a counter
