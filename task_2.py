name = 'Katya Chernova'

glasnie = ['K', 'a', 't', 'y', 'a', 'C', 'h', 'e', 'r', 'n', 'o', 'v', 'a']
glasnie_str = "_".join(glasnie)
print( glasnie_str)

s = glasnie_str
su = s.upper()
print(su)

text1 = su

ascii_upper = [ord(symbol) for symbol in text1]
print(ascii_upper)

sl = s.lower()
print(sl)

text2 = sl

ascii_lower = [ord(symbol) for symbol in text2]
print(ascii_lower)

print('maximum:', max(max(ascii_upper), max(ascii_lower)))
print('minimum:', min(min(ascii_upper), min(ascii_lower)))
