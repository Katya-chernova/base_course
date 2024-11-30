	
import random

N = 8

values1 = [random.randint(0, 100) for a in range (N)]
print(values1)
values2 = [random.randint(0, 100) for a in range (N)]
print(values2)
values3 = [random.randint(0, 100) for a in range (N)]
print(values3)


print('maximum:', max(max(values1), max(values2), max(values3)))
print('sum:', sum(values1)+sum(values2)+sum(values3))