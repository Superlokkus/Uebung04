#!/usr/bin/python
# encoding=utf-8

"""Zusatz Übung 04.6 Mersenne Primzahlsuche"""
#Markus Klemm WS12/13 Phy-BA

def PrimMersenne(p):
    """Berechnet die Mersennezahl der Ordnung gegebenen Ordnung p und gibt diese 
    zurück, wenn diese eine Primzahl ist. Ansonsten None"""
    m = 2**p - 1 #=Mersennezahl
    if (p==2):
        return m
    
    #LucasLehmerFolge Beginn
    s = [0,4]
    
    for x in (range(2,p)):
        s.append((s[x-1]**2 - 2) % m) #Primzahlentest mithilfe LucasLahmer Test
        #und Kongruenz
        if (s[x] == 0):
            return m
        
    return

def Ausgabe(p):
    """Gibt mithilfe der Funktion PrimMersenne(p), Mersenneprimzahlen in dezimal
    und binär aus. """
    mer = PrimMersenne(p)
    if (mer != None):
        print "Die Mersennezahlprimzahl der Ordnung " + str(x) + " ist: "
        print str(mer) + " in Dezimal bzw. " + str(bin(mer)) + " in Binär."


print "Folgende Mersennezahlen p-ter Ordnung sind Primzahlen:"
for x in (range(1,125)):
    Ausgabe(x)

Ausgabe(11213)