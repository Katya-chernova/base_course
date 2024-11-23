names = ["John", "Davia", "Maria"]
ages = [16,25,19]
isTeenager = [True, False, True]

users = list(zip(names, ages, isTeenager))
print(users)

print("Users age:", dict(zip(names, ages)))