from sys import stdin


words = {}
vvod = stdin
for line in vvod:
    #print(line)
    qq = line.replace('-', ' ')
    for i in ['.', ',', '!', '?', '(', ')', '   --', ' --', '\"']:
        qq = qq.replace(i, '')
    for ii in qq.split():
        if ii.lower() in words.keys():
            words[ii.lower()] += 1
        else:
            words[ii.lower()] = 1
print(' '.join(sorted(list(words.keys()), key=lambda x: (-words[x], x), reverse=False)[:50]))