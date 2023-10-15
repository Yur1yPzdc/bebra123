def predict(sreda, plrs):
    return ''


for _ in range(int(input())):
    ans = ''
    plrs = [1+i for i in range(int(input()))]
    sreda = input()
    for i in range(len(plrs) - 1):
        ans += predict(sreda=sreda[:i+1], plrs=plrs[:i+2])