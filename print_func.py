#
import sys
import numpy as np
import matplotlib.pyplot as mplot

if( len(sys.argv)!=2):
	print("No input parameter...")
	print("Usage:")
	print("1 :: plot x")
	sys.exit()

xvar=[];yvar=[]
for i in range (0,101):
	ii= -5.0 + 0.1 * i
	xvar.append(ii)

if (int(sys.argv[1])==1):
	yvar=xvar
	#print(yvar)
	mplot.plot(xvar,yvar)
	mplot.xlim(-3.0,3.0)
	mplot.show()
else:
	print("Not one")
	

