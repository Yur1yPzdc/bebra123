# 131 задача 
# вбиваешь значения с одной единицей, смотришь когда совпадет с табличным => единица на позиции таблицы (1, 2, 3) - позиция введенной единицы (a, b, c)
# зная где единица, смотрим где будет выдана 1 при двух единицах в тройке, когда одна на известной позиции
def get(a, b, c):
    # строишь функцию логических операций
    return (not a or b) and (not (a and b) or not c)

while True:
    print(int(get(*[bool(int(i)) for i in input()])))
    # 100 выдает единственный 0 как 001 из таблицы => а-3
    # 110 выдает единственную 1 как 011 из таблицы => b-2 и с-1