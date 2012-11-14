#!/usr/bin/python
# encoding=utf-8

"""Übung 04 Fibonacci"""
#Markus Klemm WS12/13 Phy-BA

def fibo(n):
    """Gibt die Ficonacci Zahl n-ter Ordnung zurück"""
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))

assert (fibo(10) == 55)

print fibo(10)
print fibo(20)
print fibo(30)
print fibo(40)