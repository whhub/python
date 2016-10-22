# if inline
print("Hello" if False else "World")

# concatenation
nfc = ["Pachkers", "49ers"]
afc = ["Ravens", "Patriots"]
print(nfc+afc)

# floor
print(5.0//2)

# power
print(2**5)

# float divide
print(.3/.1)
print(.3//.1)

# compare
print(3 > 2 > 1)
print(1 < 2 > 0)

# iterate two lists at the same time
for teamA, teamB in zip(nfc, afc):
    print(teamA + " vs. " + teamB)

# iterate with index
for index, team in enumerate(nfc):
    print(index, team)

# list creation
numbers = [1, 2, 3, 4, 5, 6]
even = [number for number in numbers if number % 2 == 0]
print(even)
print([0]*3)

# dictionary creation
print({key: value for value, key in enumerate(nfc+afc)})

# sub list
x = [1, 2, 3, 4, 5, 6]
print(x[:3])
print(x[1:5])
print(x[2:])
print(x[-3:])
print(x[::2])
print(x[1::2])

# ?FizzBuzz
for x in range(101):
    print("fizz"[x % 3 * 4::]+"buzz"[x % 5 * 4::] or x)

# Counter
from collections import Counter
print(Counter("hello"))

# itertools
from itertools import combinations
for game in combinations(nfc+afc, 2):
    print(game)

