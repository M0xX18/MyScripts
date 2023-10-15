# O(t)
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    count_1 = a.count(1)

    if a_sum >= count_1 + n and n > 1:
        print("YES")
    else:
        print("NO")
