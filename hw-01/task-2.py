""" Задача 2. Напишите программу, которая принимает на вход координаты 
двух точек и находит расстояние между ними в 2D пространстве.
A (3,6); B (2,1) -> 5,1
A (7,-5); B (1,-1) -> 7,21 """

from math import sqrt


ax = int(input("Ax: "))
ay = int(input("Ay: "))
bx = int(input("Bx: "))
by = int(input("By: "))

distance = sqrt((ax - bx)**2 + (ay - by)**2)
print(
    f"Distance between A({ax},{ay}) and B({bx},{by}) -> {round(distance, 2)}")
