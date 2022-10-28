side = int(input())
grani = int(input())


def find_0s(side):
    return pow(side-2, 3) if side > 2 else 0


def find_1s(side):
    return 6*pow(side-2, 2) if side > 2 else 0


def find_2s(side):
    return 12*(side-2) if side > 2 else 0


def find_3s(side):
    return 8 if side > 1 else 0


if grani == 0:
    print(find_0s(side))

elif grani == 1:
    print(find_1s(side))

elif grani == 2:
    print(find_2s(side))

elif grani == 3:
    print(find_3s(side))