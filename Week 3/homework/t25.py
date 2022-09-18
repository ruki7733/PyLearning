n = int(input())
total = 0
lst = []
for i in range(n):
    s = input().split()
    x, y = int(s[0]), int(s[1])
    if 90 <= x <= 140 and 60 <= y <= 90:
        total += 1
    else:
        total=0
    lst.insert(n, total)
total=max(lst)
print(total)
