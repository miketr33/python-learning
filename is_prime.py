# From Codeacademy is_prime() task.
# Took a while to get working but was all because of indentation.

def is_prime(x):
	not_prime = False

	if x <= 1:
		return False
	elif x == 2 or x == 3:
		return True
	else:
		for n in range(2, x):
			if ((x / n) % 1 == 0.0):
				not_prime = True

	if not_prime == True:
		return False
	else:
		return True

print(is_prime(5))
