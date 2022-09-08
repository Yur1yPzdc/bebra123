skobki = {}
line = ''.join([i for i in input() if i not in '1234567890-+/*'])
case = ''
for _ in range(int(input())):
    i = input()
    skobki[i[-1]] = i[0]
while True:
    for i in range(len(line)):
        q = i
        if i in skobki.keys():
            qq = skobki[line[i]]
            q -= 1
            if q < 0:
                case = f'Miss open bracket for bracket {qq}'

            if line[q] == qq:
                line = line[:i] + line[i+1:]
                line = line[:q] + line[q+1:]

            if line[q] != qq:
                case = f'Expected {qq} but {line[q]} found'

            if bool(len(case)):
                break

    w = True
    for i in list(skobki.keys()):
        if i in line:
            w = False
            break
        else:
            if i == list(skobki.keys()[-1]):
                case = f'Miss сlose bracket for bracket {line[-1]}'
            
    if bool(len(case)):
        break

    if len(line):
        break

if bool(len(case)):
    print(case)
else:
    print('Correct')
