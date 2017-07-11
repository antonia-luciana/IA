import re
import string

def parsare(filename):
	necunscute=[]
	with open(filename) as f:
		sistem=f.read()
		sistem=sistem.lower()   #asigur ca literele sunt minuscule
		for i in sistem:
			if i.isalpha() and i not in necunscute:  #stabilim care sunt necunoscutele si le punem intr-o lista
				necunscute.append(i)
			
#elinimam eventualele * folosite pt inmultire
	sistem=sistem.replace('*','')
#elinimam spatiile
	sistem=sistem.replace(' ','')
#desfacem sistemul intr-o lista de ecuatii
	ecuatii=sistem.split('\n')
#eliminam eventualele siruri vide
	ecuatii=filter(None,ecuatii)	


#definim A matricea sistemului si B matricea termenilor liberi
	A=[]
	B=[]
#parsarea propriu-zisa
	for e in ecuatii:   #parcurgem fiecare ecuatie
		nr_constanta=0   #pozitia coeficientului curent in lista de coeficienti
		constante=re.findall(r'[-]*\d+',e)   #punem toti coeficientii intr-o lista
		#print constante
		ultimul=constante[len(constante)-1]
		B.append([float(ultimul)])
		constante.remove(ultimul)
		 
		linie=[]  #linia curenta din matrice
		for n in necunscute:  #x,y,z
			#print nr_constanta
			if (n not in e):
				linie.append(float(0))
			elif e.find(n)>0 and e[e.find(n)-1].isdigit():  #daca exista coeficient  
				linie.append(float(constante[nr_constanta]))
				nr_constanta+=1
			elif  e[e.find(n)-1]=='-':  #daca gasim -, se completeaza cu -1
				linie.append(float(-1))
				
			else:
				linie.append(float(1))
		
		#print linie
		A.append(linie)	#punem linia in matrice

	return [A,B]
	

	f.close()

#print parsare('ecuatie3.txt')
'''enunt.lower()
	necunscute=re.findall(r'[a-z]+',enunt)
	necunscute=list(set(necunscute))
	
	nec=re.findall(r'[a-z]+',enunt)
		print necunscute
		numere=re.findall(r'[-]*\d+',enunt)
		matrice.append(numere[:-1])
		print numere'''