def make_equal_length(str1, str2):
	len1 = len(str1)
	len2 = len(str2)
	if len1 < len2:
		for i in range(len2 - len1):
			str1 = '0' + str1
		return len2
	elif len1 > len2:
		for i in range(len1 - len2):
			str2 = '0' + str2
	return len1 
def add_bit_strings(first, second):
	result = "" 
	length = make_equal_length(first, second)
	carry = 0 
	for i in range(length-1, -1, -1):
		first_bit = int(first[i])
		second_bit = int(second[i])
		sum = (first_bit ^ second_bit ^ carry) + ord('0')

		result = chr(sum) + result
		carry = (first_bit & second_bit) | (second_bit & carry) | (first_bit & carry)
	if carry:
		result = '1' + result

	return result

def multiple_single_bit(a, b):
	return int(a[0]) * int(b[0])

def multiple(X, Y):
	n = max(len(X), len(Y))
	X = X.zfill(n)
	Y = Y.zfill(n)
	if n == 0: return 0
	if n == 1: return int(X[0])*int(Y[0])

	fh = n//2 
	sh = n - fh 
	Xl = X[:fh]
	Xr = X[fh:]
	Yl = Y[:fh]
	Yr = Y[fh:]
	P1 = multiple(Xl, Yl)
	P2 = multiple(Xr, Yr)
	P3 = multiple(str(int(Xl, 2) + int(Xr, 2)), str(int(Yl, 2) + int(Yr, 2)))
	return P1*(1<<(2*sh)) + (P3 - P1 - P2)*(1<<sh) + P2

if __name__ == '__main__':
	print(multiple("1100", "1010"))
	print(multiple("110", "1010"))
	print(multiple("11", "1010"))
	print(multiple("1", "1010"))
	print(multiple("0", "1010"))
	print(multiple("111", "111"))
	print(multiple("11", "11"))
