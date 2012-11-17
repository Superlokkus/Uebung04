#!/usr/bin/python
# encoding=utf-8

"""Zusatz Übung 04.6 Mersenne Primzahlsuche"""
#Markus Klemm WS12/13 Phy-BA

def PrimMersenne(p):
    """Berechnet die Mersennezahl der Ordnung gegebenen Ordnung p und gibt diese 
    aus, wenn diese eine Primzahl ist. Benutzt hierfür die LucasLehmerFolge 
    Funktion."""
    m = 2**p - 1 #=Mersennezahl
    if (p==2):
        return m
    
    #LucasLehmerFolge
    s = [0,4]
    for x in (range(2,p)):
        s.append(s[x-1]**2 - 2)
    
    #LucasLehmerTest
    for x in (range(3,p)):
        if (s[x-1] % m ==0):
            return m
    return

        
for x in (range(1,25)):
    print PrimMersenne(x)
    
print "Große Zahl"    
print PrimMersenne(11213)