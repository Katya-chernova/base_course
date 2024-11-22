
def calculate_function(func, a, b, n):
 x_values = [a + i * (b - a) / (n - 1) for i in range(n)] 
 y_values = [func(x) for x in x_values]
 return y_values

def square(x):
 return x**2

a = -2
b = 2
n = 5

result = calculate_function(square, a, b, n)
print(result)









