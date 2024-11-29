name = "Katya Chernova Vladimirovna"
print(name)

upper_case_list = [ord(symbol) for symbol in name.upper()]
print(upper_case_list)

lower_case_list = [ord(symbol) for symbol in name.lower()]
print(lower_case_list)

sum_upper = sum(upper_case_list)
print(f'Сумма ASCII кодов в верхнем регистре: {sum_upper}')

sum_lower = sum(lower_case_list)
print(f'Сумма ASCII кодов в нижнем регистре: {sum_lower}')




