import math
print("a:")
a = int(input())
print("b")
b = int(input())
print("c:")
c = int(input())
r1 = ""
r2 = ""
if b ** 2 - 4 * a * c >= 0: 
    r1 = str(((-1 * b) + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
    r2 = str(((-1 * b) - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
if r1 == r2:
    print("r = "r1)
elif r1 == "":
    print("no root")
else:
    print("r1 = " + r1 + "  r2 = " + r2)