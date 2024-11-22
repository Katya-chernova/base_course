def quadratic(a, b, n):
    for i in range(n):
     x = a + i * (b - a) / n 
         
    return x

result = quadratic(1, 5, 10)
print(result)



