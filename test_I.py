skobki = {}
line = ''.join([i for i in input() if i not in '1234567890-+/*'])
case = ''
for i in range(int(input())):
    skobki[i[-1]] = i[0]
while True:
    q = i
    for i in range(len(line)):
        if i in skobki.keys():
            qq = skobki[line[i]]
            q -= 1
            if q < 0:
                case = f'Miss open bracket for bracket {qq}'

            if line[q] == qq:
                line = line[:i] + line[i+1:]
                line = line[:q] + line[q+1:]

            if line[q] != qq:
                case = f'Miss open bracket for bracket {qq}'
            if bool(len(case)):
                break
    if bool(len(case)):
                break
    
