q = input()
w = set()
for i in range(len(q)):
    w.add(q[i])
    b = []
    for qq in w:
        b.append(qq)
    if sorted(b) == [0,1,2,3,4,5,6,7,8,9]:
        print(i+1)
        break
else:
    print('fail')