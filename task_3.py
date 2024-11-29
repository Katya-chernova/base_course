import time

M = 2
N = 5

timer = time.time()

for a in range(M + 1):
    print(f"Внешний цикл: {a}")
    time.sleep(1)

    for b in range(N + 1):
        print(f'Внутренний цикл: {b}')
    time.sleep(1)   
 

print(f'Общее время: {time.time() - timer}, секунд') 

