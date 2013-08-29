# -*- coding: utf-8 -*-

import sys
import time


sys.argv=sys.argv[1:]

def read_file(index):
    global dosya, file, yazi, n, a, i
    dosya = sys.argv[index]
    file = open(dosya, "r")
    yazi = file.readlines()
    yazi.reverse()
    n = 0
    a = []
    for i in yazi:
        a.append(i)
        n += 1
        if n == 10:
            break
    a.reverse()
    for i in a:
        print i,
    file.close()

if sys.argv[0]=="-n":
    sayi = sys.argv[1]
    dosya = sys.argv[2]
    file = open(dosya,"r")
    yazi = file.readlines()
    yazi.reverse()
    n=0
    for i in yazi:
        print i
        n+=1
        if n==int(sayi):
            break
elif sys.argv[0]=="-f":
    fileBytePos = 0
    read_file(1)
    while True:
        file = open(dosya, "r")
        file.seek(fileBytePos)
        yazi = file.readlines()
        if yazi.__len__() > 0:
            print yazi[yazi.__len__()-1],
            fileBytePos = file.tell()
        file.close()
        time.sleep(1)
else:
    read_file(0)