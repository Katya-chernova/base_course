name = "Katya Chernova Vladimirovna"
print(name)

s = name
su = s.upper()
print(su)
upper = [ord(symbol) for symbol in name.upper()]
print(upper)

sl = s.lower()
print(sl)
lower = [ord(symbol) for symbol in name.lower()]
print(lower)

sum_upper = sum(upper)
print(f'Сумма ASCII кодов в верхнем регистре: {sum_upper}')

sum_lower = sum(lower)
print(f'Сумма ASCII кодов в нижнем регистре: {sum_lower}')




