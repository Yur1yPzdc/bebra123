for _ in range(int(input())):
    length = int(input())
    line = tuple(i for i in input())
    hren = 0
    ans = ''
    for i in line:
        if i == '0':
            ans += '+'
        else:
            if hren == 0:
                ans += '+'
                hren += 1
            else:
                ans += '-'
                hren -= 1
    print(ans[1:])