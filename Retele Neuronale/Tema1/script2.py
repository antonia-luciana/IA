import parsare
import copy

A=[]
B=[]

[A,B]=parsare.parsare("ecuatie.txt")

#4. Determinant
def determinant(A):
	if len(A)==2:
		return float(A[0][0])*float(A[1][1])-float(A[0][1])*float(A[1][0])
	else:
		D=0
		for i in range(0,len(A)):
			M=copy.copy(A)
			if i%2==0:				
				D=D+float(A[0][i])*determinant(minor(M,0,i))
			else:
				D=D-float(A[0][i])*determinant(minor(M,0,i))
	return D		




	
def minor(Matrice,i,j):  #matrice in care s-a sters linia i si coloana j
	Minor=[]
	Minor[:i]=Matrice[:i]
	Minor[i:]=Matrice[i+1:]
	
	Minor2=[x[:] for x in Minor]
	
	for rand in Minor2:
		del rand[j]
	
	return Minor2
	

def transpusa(Matrice):
	T=[]
	for j in range(len(Matrice[0])):
		rand=[]
		for i in range(len(Matrice)):
			rand.append(0)
		T.append(rand)
	print T
	for i in range(0,len(Matrice)):
		for j in range(0,len(Matrice)):
			T[i][j]=Matrice[j][i]
	
	return T

def aStelat(Matrice):   #calculeaza matricea A^* = (-1)^(i+j)*minor(A,i,j)
	AStea=[]
	for i in range(len(Matrice)):
		rand=[]
		for j in range(len(Matrice)):
			if (i+j)%2==1:
				rand.append(-determinant(minor(Matrice,i,j)))
			else:
				rand.append(determinant(minor(Matrice,i,j)))
		AStea.append(rand)
	return AStea

	
def inversa(Matrice):
	det=determinant(Matrice)
	AStea=[]
	AStea=aStelat(transpusa(Matrice))
	for i in range(len(AStea)):
		for j in range(len(AStea)):
			AStea[i][j]=AStea[i][j]/det
	return AStea
	


def inmultireAB(A,B):   #inmultire dintre matrice ecuatiei si un vectorul coloana al termenilor liberi: A*B
	Produs=[]
	print A
	print B
	for i in range(len(A)):
		rez=0
		for j in range(len(A[0])):
			#print "Elem A "+str(A[i][j])+" Elem B "+str(B[j][0])
			rez=rez+(float(A[i][j])*float(B[j][0]))
		Produs.append(rez)
	return Produs
		
print A
print B
print determinant(A)
if determinant(A)>0:
	print inmultireAB(inversa(A),B)
else:
	print "Sistemul nu are solutie"


	'''	
def puneSemne(Matrice):  #minusurile pt matricea adjuncta (-1)^i+
	for i in range(len(Matrice)):
		for j in range(len(Matrice)):
			if (i+j)%2==1:
				Matrice[i][j]=-(Matrice[i][j])
	return Matrice
'''

'''
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
			line.append(float(A[l1[0]][l2[0]])*float(A[l1[1]][l2[1]])+(float(A[l1[0]][l2[1]])*float(A[l1[1]][l2[0]])))
		rez.append(line)
	return rez
	
#rez=matrice_minori(A)
#print rez

#2. Matrix of Cofactors
def semne(A):
	A[0][1]=-(A[0][1])
	A[1][0]=-(A[1][0])
	A[1][2]=-(A[1][2])
	A[2][1]=-(A[2][1])
	return A
	

#3.Adjugate
def adjugate(A):
	aux=A[0][1]
	A[0][1]=A[1][0]
	A[1][0]=aux
	
	aux=A[2][0]
	A[2][0]=A[0][2]
	A[0][2]=aux
	
	aux=A[1][2]
	A[1][2]=A[2][1]
	A[2][1]=aux
	
	return A
	
#y=semne(rez)
#print y
#print adjugate(semne(rez))
#print adjugate(y)
'''