a = int(input())
b = int(input())
if b == 0:
    print("Делить на ноль нельзя")
elif a % b == 0:
    print(a/b)
else:
    print(a%b)
остаток = a % b
частное = a//b
print( f"Остаток: {остаток} ")
print(f"Частное: {частное}")