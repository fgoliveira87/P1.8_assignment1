#
import sys
import numpy as np
import matplotlib.pyplot as mplot

if( len(sys.argv)!=2):
	print("No input parameter...")
	print("Must input an integer.")
	sys.exit()

xvar=[];yvar=[]
for i in range (0,101):
	ii= -5.0 + 0.1 * i
	xvar.append(ii)

if (int(sys.argv[1])==1):
	yvar=xvar
	#print(yvar)
	mplot.plot(xvar,yvar)
	mplot.show()
elif (int(sys.argv[1])==2):
	yvar= [np.sin(x) for x in xvar]
	#print(yvar)
	mplot.plot(xvar,yvar)
	mplot.show()
elif (int(sys.argv[1])==3):
	yvar= [np.cos(x) for x in xvar]
	#print(yvar)
	mplot.plot(xvar,yvar)
	mplot.show()
elif (int(sys.argv[1])==4):
	yvar= [np.tan(x) for x in xvar]
	#print(yvar)
	mplot.plot(xvar,yvar)
	mplot.show()	
else:
	print("Try for 1, 2, 3 or 4")
