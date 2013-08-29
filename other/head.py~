# -*- coding: utf-8 -*-

import sys


sys.argv=sys.argv[1:]

if sys.argv[0]=="-n":
    sayi = sys.argv[1]
    dosya = sys.argv[2]
    file = open(dosya,"r")
    yazi = file.readlines()
    n=0
    for i in yazi:
        print i
        n+=1
        if n==int(sayi):
            break
else:
    dosya = sys.argv[0]
    file = open(dosya,"r")
    yazi = file.readlines()
    n=0
    for i in yazi:
        print i
        n+=1
        if n==10:
            break

