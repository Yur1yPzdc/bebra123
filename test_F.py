q = list(map(int, input().split()))
m, n = q[0], q[1]
a = input().split()
b = input().split()
print(str(len(list(i for i in b if i not in a))) + '\n' + ' '.join(list(i for i in b if i not in a)))