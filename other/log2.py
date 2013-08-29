# -*- coding: utf-8 -*-

import sys

file = open("test.log","r")
yazi = file.readline()

print yazi

yazi = str(file.readline())
a=0

def general():
    global a, yazi
    yazi = yazi[a+1:]
    a = yazi.find(" ")



a = yazi.find(" ")
ip = yazi[:a]
general()
unidentity = yazi[:a]
general()
frank = yazi[:a]
general()
request_was_received = yazi[:a]


print ip
print unidentity
print frank
print request_was_received