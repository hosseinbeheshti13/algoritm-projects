def sterling_partition(n, r):
    if n == 0 and r == 0:
        return 1
    if n < 0 or r == 0:
        return 0
    return r * sterling_partition(n-1, r) + sterling_partition(n-1, r-1)

n = 7
r = 4
result = sterling_partition(n, r)
print(f"S({n}, {r}) = {result}")
