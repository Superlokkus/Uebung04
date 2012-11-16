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
    
    for x in (range(3,p)):
        if (LucasLehmerFolge(x-1) % m ==0):
            return m
    return

def LucasLehmerFolge(p):
    """Gibt das Element p der Folge s des Lucas Lehmer Primzahlentests zurück,
    undefinierte Elemente = 0"""
    s = [0,4]
    for x in (range(2,p+1)):
        s.append(s[(x-1)]**2 - 2)
    return s[p]
        
for x in (range(1,25)):
    print PrimMersenne(x)
    
print "Große Zahl"    
print PrimMersenne(11213)