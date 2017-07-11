import parsare

from numpy import matrix
from numpy import linalg
import numpy as np

A=[]
B=[]

[A,B]=parsare.parsare("ecuatie.txt")

A=matrix(A)
B=matrix(B)

print A
print B
print A.T

if np.linalg.det(A)>0:
	print "Sistemul are solutia "+str(A.I*B)
else:
	print "Sistemul nu are solutie"
	


#print str(np.linalg.det(A))

''''
#1. Matricea minorilor
def matrice_minori(A):
	rez=[]
	for i in range(0,len(A)):
		line=[]
		for j in range(0,len(A)):
			l1=list(range(0,len(A)))
			l2=list(range(0,len(A)))
			l1.remove(i)
			l2.remove(j)
			line.append(float(A[l1[0],l2[0]])*float(A[l1[1],l2[1]])+(float(A[l1[0],l2[1]])*float(A[l1[1],l2[0]])))
		rez.append(line)
	print rez
	
matrice_minori(A)

#2. Semne
'''
