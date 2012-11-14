#!/usr/bin/python
# encoding=utf-8

import time

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

def ausgabe(n):
    """Funktion zur Ausgabe der n-ten Fibonacci Zahlen mit Zeitverbrauch"""
    t1 = time.time()
    print "Die Fibonaccizahl der  " + str(n) + ".ten Ordnung ist:"
    print fibo(n)
    print "Und benötigte " + str(t1 - time.time()) + " Sekunden"


for x in (range(10,40,10)): #Ausgabe der geforderten Fibonaccizahlen
    ausgabe(x)
