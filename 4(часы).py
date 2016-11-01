#!/usr/bin/env python3

a = int(input("Минуты : "))

b = a % (60 * 24) // 60
c = a % 60

print(" Время: ", b, c)
