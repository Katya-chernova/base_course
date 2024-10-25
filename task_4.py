import numpy as np

N = 2
M = 3

trigonometry_array = np.zeros((N, M))  

for i in range(N):
    for j in range(M):
        trigonometry_array[i, j] = np.sin(N * i * M * j + 1)
        if trigonometry_array[i, j] < 0:  
            trigonometry_array[i, j] = 0

print(trigonometry_array)