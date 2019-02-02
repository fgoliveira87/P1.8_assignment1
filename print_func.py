#
import sys
import numpy as np
import matplotlib.pyplot as mplot

if( len(sys.argv)!=2):
	print("No input parameter...")
	sys.exit()
	
xvar=[];yvar=[]
for i in range (0,101):
	ii= -5.0 + 0.1 * i
	xvar.append(ii)
	
if (int(sys.argv[1])==1):
	yvar=xvar
#print (yvar)

mplot.plot(xvar,yvar)
mplot.show()
