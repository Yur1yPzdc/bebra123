a, b, c = int(input()), int(input()), int(input())
min_delta = min([b+c-a, a+c-b, a+b-c])
print(min_delta)