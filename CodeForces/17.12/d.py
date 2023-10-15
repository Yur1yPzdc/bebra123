for _ in range(int(input())):
    kolvo, dlina = tuple(map(int, input().split()))
    q = [list(map(int, input().split())) for _ in range(kolvo)]
    qq = [sum(i) for i in q]
    amount = sum(qq)
    ans = 0
    answers = []

    if amount % kolvo != 0:
        print(-1)
        continue
    nado = amount // kolvo

    for i in q:
        if sum(i) == nado:
            continue
        if sum(i) > nado:
            for ii in q:
                if sum(i) == nado:
                    break
                if ii != i and sum(ii) < nado:
                    for iii in range(dlina):
                        if i[iii] == 1 and ii[iii] == 0:
                            i[iii] = 0
                            ii[iii] = 1
                            ans += 1
                            answers.append((q.index(ii)+1, q.index(i)+1, iii+1))
                        if sum(ii) == nado or sum(i) == nado:
                            break
                        continue
                
    print(ans)
    for i in answers:
        print(*i, sep=' ')