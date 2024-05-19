def multiply_polynomials_naive(p, q):
    n = len(p)
    m = len(q)
    result = [0] * (n + m - 1)
    
    for i in range(n):
        for j in range(m):
            result[i + j] += p[i] * q[j]
    
    return result

p = [2, 1]
q = [3, 2, 1]  

result = multiply_polynomials_naive(p, q)
print(result)  
