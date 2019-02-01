#
import sys
import numpy as np
import matplotlib.pyplot as mplot

if( len(sys.argv)!=2 or int(sys.argv[1])>3 or int(sys.argv[1])<1):
	print("No input parameter...")
	print("Usage:")
	print("1 :: plot x")
	#print("2 :: plot x^2")
	#print("3 :: plot x^3")
	print("2 :: plot exp(x)")
	print("3 :: plot sqrt(|x|)")  
	sys.exit()

xvar=[];yvar=[]
for i in range (0,101):
	ii= -5.0 + 0.1 * i
	xvar.append(ii)

if (int(sys.argv[1])==1):
	yvar=xvar

elif (int(sys.argv[1])==2):
	yvar=[np.exp(x) for x in xvar]

elif (int(sys.argv[1])==3):
	yvar=[np.sqrt(abs(x)) for x in xvar]

mplot.plot(xvar,yvar)
mplot.xlim(-3.0,3.0)
mplot.show()

	

