t = int(input())

for _ in range (t):
    n = int(input())
    if n % 2 == 1:
        for i in range(1, n + 1):
            print(1, end=" ")
        print()
    else:
        for i in range(1, n - 2 + 1):
            print(2, end=" ")
        print(1, 3)
