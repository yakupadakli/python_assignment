# -*- coding: utf-8 -*-
import sys
import re

try:	
	sys.argv = sys.argv[1:]
	file_name = sys.argv[0]
	target_file_name = sys.argv[1]
except IndexError:
	print "Lütfen dosya adını argüman olarak giriniz"
	exit()

try:
	source = open(file_name,"r")
	target = open(target_file_name,"a")

	for line in source:
		target.write(line)

	source.close()
	target.close()

except IOError:
	print "Böyle bir dosya yok"