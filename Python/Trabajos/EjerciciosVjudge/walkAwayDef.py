def f(x, y, d):
    e = (y - x) % d == 0
    return (y - x) // d + 1 - e

def solve():
    n, m, d = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    start = 0
    if arr[0] != 1:
        start = 1
        arr.insert(0, 1)
    
    arr.append(n + 1)
    n = len(arr)
    ans = 0
    for i in range(1, n):
        ans += f(arr[i - 1], arr[i], d)
    
    a2 = ans
    newans = ans
    
    for i in range(1, n - 1):
        cur = f(arr[i - 1], arr[i + 1], d) - f(arr[i - 1], arr[i], d) - f(arr[i], arr[i + 1], d)
        newans = a2 + cur
        ans = min(ans, newans)
    
    cnt = 0
    for i in range(1, n - 1):
        cur = f(arr[i - 1], arr[i + 1], d) - f(arr[i - 1], arr[i], d) - f(arr[i], arr[i + 1], d)
        newans = a2 + cur
        if newans == ans:
            cnt += 1
    
    if ans == a2 and start == 0:
        cnt += 1
    
    print(ans, cnt)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

