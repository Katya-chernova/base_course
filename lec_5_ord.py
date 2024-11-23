text = "Katya"

for symbol in text:
    print(ord(symbol), end =";")
print()

codes = [200, 345, 688, 23433]
symbol = ""

for code in codes:
    symbol += chr(code)

print(symbol)