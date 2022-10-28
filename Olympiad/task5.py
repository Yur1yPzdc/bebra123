n = int(input())
powers = [int(input()) for _ in range(n)]
ans = ''
for i in range(n):
    pos = i + 1
    poses = []
    f = True
    while pos > 0 and pos < n+1:
        if pos in poses:
            ans += 'U'
            f = False
            break
        poses.append(pos)
        pos += powers[pos-1]
    if f:
        ans += 'R' if pos >= n+1 else 'L'
print(ans)