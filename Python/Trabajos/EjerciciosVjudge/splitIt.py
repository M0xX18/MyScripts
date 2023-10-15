# O(t*k)

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    if 2 * k >= n:
        print("NO")
    else:
        for i in range(k):
            if s[i] == s[n - 1 - i]:
                continue
            else:
                print("NO")
                break
        else:
            print("YES")
