""" Задача 3. Напишите программу, которая по заданному номеру четверти,
 показывает диапазон возможных координат точек в этой четверти (x и y).
1 -> x > 0, y > 0 """

q = int(input("Enter quarter: "))

if q == 1:
    s = "x > 0, y > 0"
elif q == 2:
    s = "x > 0, y < 0"
elif q == 3:
    s = "x < 0, y < 0"
elif q == 4:
    s = "x < 0, y > 0"
else:
    s = "No such quarter"

print(s)
