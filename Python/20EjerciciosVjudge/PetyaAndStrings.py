# O(1)
primera = input().lower()
segunda = input().lower()

if primera < segunda:
    print("-1")
elif primera > segunda:
    print("1")
else:
    print("0")
