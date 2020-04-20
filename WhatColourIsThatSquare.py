pos = input()
if (pos[0] == "a" or pos[0] == "c" or pos[0] == "e" or pos[0] == "g") and int(pos[1]) % 2 == 0:
    print("White")
elif (pos[0] == "b" or pos[0] == "d" or pos[0] == "f" or pos[0] == "h") and int(pos[1]) % 2 == 1:
    print("White")
else:
    print("Black")