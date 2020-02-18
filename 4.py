def string2ascii(s):
	ascii = [ord(c) for c in s]
	ascii = int("".join(map(str, ascii)))
	return ascii

def checkPrime(number):
	if number > 1:
		for i in range (2, number//2):
			if (number % i) == 0:
				print("", number, "is not a prime number")
				break
		else:
			print("", number, "is a prime number")
	else:
		print("", number, "is not a prime number")

print()
s = str(input(" Enter a string: "))
ascii = string2ascii(s)

print()
print("", "Ascii code: ", ascii)
print()
checkPrime(ascii)

