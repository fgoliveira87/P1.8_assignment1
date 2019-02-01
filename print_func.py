#
import sys
import numpy as np

if( len(sys.argv)!=2):
	print("No input parameter...")
	print("Must input an integer.")
	sys.exit()

x=[];y=[]
for i in range (0,101):
	ii= -5.0 + 0.1 * i
	x.append(ii)

if (int(sys.argv[1])==1):
	y=x
	print(y)
else:
	print("not one")
	

