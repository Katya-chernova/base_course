symbols = "python"
symbol_codes = [ord(symbol) for symbol in symbols]
print(symbol_codes)

symbols = 'snake'
symbol_codes = (ord(symbols) for symbol in symbols)
print(symbol_codes)

for object in symbol_codes:
    print(object)