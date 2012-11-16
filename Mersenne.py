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
    if (p == 1):
        return 4
    elif(p<1):
        return 0
    else:
        return (LucasLehmerFolge(p-1)**2 - 2)

for x in (range(1,10)):
    print PrimMersenne(x)