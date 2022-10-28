stroki, stolbci, dni = int(input()), int(input()), int(input())
y_x = []
for _ in range(dni):
    y_x.append((int(input()), int(input())))
x_min = pow(10, 9)
y_min = pow(10, 9)
for i in y_x:
    y_min = i[0] if i[0] < y_min else y_min
    x_min = i[1] if i[1] < x_min else x_min
print(x_min*y_min, dni)