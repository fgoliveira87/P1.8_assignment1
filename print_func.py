#
import sys
import numpy as np
import matplotlib.pyplot as mplot

if( len(sys.argv)!=2):
	print("No input parameter...")
	print("Usage:")
	print("1 :: plot x")
	sys.exit()

def f1(x):
	return xvar
def f2(x):
	return x*x
def f3(x):
	return x*x*x

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
	yvar= [x*x for x in xvar]
	#print(yvar)
	mplot.plot(xvar,yvar)
	mplot.show()
elif (int(sys.argv[1])==3):
	yvar= [x*x*x for x in xvar]
	#print(yvar)
	mplot.plot(xvar,yvar)
	mplot.show()
else:
	print("Try for 1, 2 or 3")
	

