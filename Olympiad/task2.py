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


match grani:
    case 0:
        print(find_0s(side))

    case 1:
        print(find_1s(side))

    case 2:
        print(find_2s(side))

    case 3:
        print(find_3s(side))