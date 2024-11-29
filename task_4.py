def function(a, b, N):

  x = (b - a) / (N - 1)
  y_values = []
  for i in range(N):
    x = a + i * x
    y_values.append(x**2)
  return y_values

a = 1
b = 5
N = 4
result = function(a, b, N)
print(result)





