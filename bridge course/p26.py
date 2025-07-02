def is_armstrong(n):
	digits=[int(d) for d in str(n)]
	return n ==sum(d**len(digits) for d in digits)
print(is_armstrong(153))
