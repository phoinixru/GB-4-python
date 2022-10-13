"""
Задача 1. Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и выводит название этого дня недели.

1 –> Понедельник
10 –> Нет такого дня
7 –> Воскресение
 """

day = int(input("Enter day of the week: "))
weekDays = {1: "Monday", 2: "Tuesday", 3: "Wendsday",
            4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

if day in weekDays:
    print(weekDays[day])
else:
    print("No such day")
