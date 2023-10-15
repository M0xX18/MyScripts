# O(t*(n/2))
t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
    elif n % 2 == 1:
        print(-1)
    else:
        for i in range(2, n + 1, 2):
            print(i, i - 1, end=" ")
