hull = set()
def findSide(p1, p2, p):
	val = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])

	if val > 0:
		return 1
	if val < 0:
		return -1
	return 0
def lineDist(p1, p2, p):
	return abs((p[1] - p1[1]) * (p2[0] - p1[0]) -
			(p2[1] - p1[1]) * (p[0] - p1[0]))
def quickHull(a, n, p1, p2, side):

	ind = -1
	max_dist = 0
	for i in range(n):
		temp = lineDist(p1, p2, a[i])
		
		if (findSide(p1, p2, a[i]) == side) and (temp > max_dist):
			ind = i
			max_dist = temp
	if ind == -1:
		hull.add("$".join(map(str, p1)))
		hull.add("$".join(map(str, p2)))
		return
	quickHull(a, n, a[ind], p1, -findSide(a[ind], p1, p2))
	quickHull(a, n, a[ind], p2, -findSide(a[ind], p2, p1))

def printHull(a, n):
	if (n < 3):
		print("Convex hull not possible")
		return
	min_x = 0
	max_x = 0
	for i in range(1, n):
		if a[i][0] < a[min_x][0]:
			min_x = i
		if a[i][0] > a[max_x][0]:
			max_x = i
	quickHull(a, n, a[min_x], a[max_x], 1)
	quickHull(a, n, a[min_x], a[max_x], -1)

	print("The points in Convex Hull are:")
	
	for element in hull:
		x = element.split("$")
		print("(", x[0], ",", x[1], ") ", end = " ")

# Driver code
a = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]]
n = len(a)
printHull(a, n)