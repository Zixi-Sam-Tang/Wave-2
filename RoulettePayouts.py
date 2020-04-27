import random
num = random.randint(1, 38)
if num <= 36: print("The spin resulted in " + str(num) + "...")
elif num == 37: print("The spin resulted in 0...")
else: print("The spin resulted in 00...")
if num != 37 and num != 38:
    print("Pay", num)
    if (num < 10 and num % 2 == 1) or (num > 10 and num <= 18 and num % 2 == 0) or (num > 18 and num < 30 and num % 2 == 1) or (num >= 30 and num <= 36 and num % 2 == 0): print("Pay Red")
    else: print("Pay Black")
    if num % 2 == 0: print("Pay Even")
    else: print("Pay Odd")
    if num >= 19 and num <= 36: print("Pay 19 to 36")
    else: print("Pay 1 to 18")
else:
    if num == 37: print("Pay 0")
    else: print("Pay 00")