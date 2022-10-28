t = int(input())
d = int(input())
p0 = 1
p = 1
q = 0
while p*(t-1) <= d:
    q -= p*(t-1)-d
    p += 1
print(q)