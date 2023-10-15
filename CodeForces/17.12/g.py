def f(q, w):
    first, last = [i for i in q if i[0] == w[0]], [i for i in q if i[1] == w[1]]
    


otr, zapr = tuple(map(int, input().split()))
otrezki = []
for i in range(otr):
    otrezki.append(tuple(map(int, input().split())))
for _ in range(zapr):
    zapros = tuple(map(int, input().split()))
    obed = [i for i in otrezki if i[0] >= zapros[0] and i[1] <= zapros[1]]
    print(obed)