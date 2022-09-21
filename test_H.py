from re import S


skobki = {}
line = ''.join([i for i in input() if i not in '1234567890-+/*'])
verdict = ''
for _ in range(int(input())):
    i = input()
    skobki[i[-1]] = i[0]
skobki1 = list(skobki.keys())
while True:
    if len(line) == 1:
        if line in skobki.values():
            verdict = f'Miss сlose bracket for bracket {line}'
    if len(verdict) != 0:
        break
    if len(line) == 0:
        break
    for i in range(len(line)):
        if line[i] in skobki1:
            if i == 0:
                verdict = f'Miss open bracket for bracket {line[i]}'
            if line[i-1] == skobki[line[i]]:
                line = line[:i-1] + line[i+1:]
                print(line)
                break
            else:
                if line[i-1] in skobki.values():
                    verdict = f'Expected {skobki[line[i]]} but {line[i-1]} found'
                else:
                    verdict = f'Miss open bracket for bracket {line[i]}'
            if len(verdict) != 0:
                break
if bool(len(verdict)):
    print(verdict)
else:
    print('Correct')