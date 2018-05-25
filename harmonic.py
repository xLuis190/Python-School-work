def harmonic(n):
	i = 1
	if(n > 1):
            return n / 2
        elif(i == n):
            return
        i + harmonic(i+1)

print(harmonic(10))
