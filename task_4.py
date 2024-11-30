import numpy as np

def function(a, b, N):
    x = np.linspace(a, b, N)
    y = x**2
    # x = (b - a) / (N - 1)
    # y_values = []
    # for i in range(N):
    #     x = a + i * x
    #     y_values.append(x**2)
    # return y_values
    return y


result = function(1, 5, 100)
print(result)





