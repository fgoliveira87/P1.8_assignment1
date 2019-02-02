#
import sys
import numpy as np
import matplotlib.pyplot as mplot

if( len(sys.argv)!=2 or int(sys.argv[1])>1 or int(sys.argv[1])<1):):
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
#print (yvar)
elif (int(sys.argv[1])==2):
	yvar= [x*x for x in xvar]

elif (int(sys.argv[1])==3):
	yvar= [x*x*x for x in xvar]

mplot.plot(xvar,yvar)
mplot.show()
