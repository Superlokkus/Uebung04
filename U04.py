#!/usr/bin/python
# encoding=utf-8

import time

"""Übung 04 Fibonacci"""
#Markus Klemm WS12/13 Phy-BA

N=0
def fibo(n):
    """Gibt rekursiv die Ficonacci Zahl n-ter Ordnung zurück"""
    if (n == 0):
        global N
        N += 1
        return 0
    elif (n == 1):
        global N
        N += 1
        return 1
    else:
        global N
        N += 1
        return (fibo(n-1) + fibo(n-2))
        
def ifibo(n):
    """Gibt iterativ die Fibonacci Zahl n-ter Ordnung zurück"""
    mylist = []
    mylist.append(0)
    mylist.append(1)
    
    for x in (range(2,n+1)):
        mylist.append(mylist[x-1] + mylist[x-2])
    return mylist[n]
    
assert (ifibo(10) == 55)

assert (fibo(10) == 55)

def ausgabe(n):
    """Funktion zur Ausgabe der n-ten Fibonacci Zahlen mit Zeitverbrauch"""
    t1 = time.time()
    print "Die Fibonaccizahl der  " + str(n) + ".ten Ordnung ist:"
    print fibo(n)
    print "Und benötigte " + str(t1 - time.time()) + " Sekunden und rufte ",
    print str(N) + " mal die Funktion auf"


for x in (range(10,40,10)): #Ausgabe der geforderten Fibonaccizahlen
    print "----Ausgabe mithilfe der rekursiven Funktion----"
    ausgabe(x)
    
    
def iausgabe(n):
    """Funktion zur Ausgabe der n-ten Fibonacci Zahlen iter.mit Zeitverbrauch"""
    t1 = time.time()
    print "Die Fibonaccizahl der  " + str(n) + ".ten Ordnung ist:"
    print ifibo(n)
    print "Und benötigte " + str(t1 - time.time()) + " Sekunden und rufte ",
    print str(N) + " mal die Funktion auf"


for x in (range(10,40,10)): #Ausgabe der geforderten Fibonaccizahlen interativ
    iausgabe(x)
