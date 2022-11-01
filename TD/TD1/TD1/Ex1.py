for i in range(1, 10):
    for j in range(1, 10-i):
        print(" ", end="")
    for j in range(1, i+1): #ou i
        print(j, end="")
    for j in range(11-i, 10): #ou 10-i
        print(10-j, end="")
    print()