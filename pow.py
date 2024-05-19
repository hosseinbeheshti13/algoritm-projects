def power(x, y):

	if (y == 0):
		return 1
	elif (int(y % 2) == 0):
		return (power(x, int(y / 2)) *
				power(x, int(y / 2)))
	else:
		return (x * power(x, int(y / 2)) *
				power(x, int(y / 2)))
if __name__ == "__main__":
	x = 4
	y = 4
	print(power(x, y))

