#!/usr/bin/python
# encoding=utf-8

"""Zusatz Übung 04.6 Mersenne Primzahlsuche"""
#Markus Klemm WS12/13 Phy-BA

def PrimMersenne(p):
    """Berechnet die Mersennezahl der Ordnung gegebenen Ordnung p und gibt diese 
    aus, wenn diese eine Primzahl ist. Benutzt hierfür die LucasLehmerFolge 
    Funktion."""
    m = 2**p - 1 #=Mersennezahl
    
    if (p>=3 & LucasLehmerFolge(p-1) % m ==0): #Prüfung ob Primzahl
        return m
    elif (p==2):
        return m
    else:
        return

def LucasLehmerFolge(p):
    """Gibt das Element p der Folge s des Lucas Lehmer Primzahlentests zurück,
    undefinierte Elemente = 0"""
    s = [0,4]
    for x in (range(2,p)):
        s.append(s[(x-1)]**2 - 2)
    return s
        
print LucasLehmerFolge(10)

#for x in (range(1,1000)):
 #   print PrimMersenne(x)