N = int(input())

for i in range(1, N + 1, 1):
    for _ in range(N - i):
        print(" ",end="")
    for _ in range(i):
        print("*",end="")
    print()  