import pickle
import gzip
import json
import simplejson
import numpy as np
import time

global train_set, valid_set, test_set
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = pickle.load(f)
f.close()
labels=np.array(train_set[1])
train_set=np.array(train_set[0])
labels_test=np.array(test_set[1])
test_set=np.array(test_set[0])

def activation(input):
    if input>0: return 1
    return 0


def perceptron(cifra):
    allClasified=False
    nr_iter=10

    w = np.array([0] * 784)
    learn = 0.1
    bias = 0.5

    while nr_iter>0 and allClasified==False:
        for i in range(len(train_set)):
            z=np.sum(train_set[i]*w)+bias
            output=activation(z)
            if labels[i]==cifra:
                t=1
            else:
                t=0
            inmultire=np.multiply((t-output)*learn,train_set[i])
            w=np.add(inmultire,w)
            bias=bias+(t-output)*learn
            if output!=t:
                allClasified=False
        nr_iter-=1

    return w,bias

global ws,bs
ws={}
bs={}

def antrenament():
    for cifra in range(10):
        w, b = perceptron(cifra)
        ws["w" + str(cifra)] = np.array(w)
        bs["b" + str(cifra)] = b

def test():
    nr_corecte=0
    for i in range(len(test_set)):
        raspunsuri=[]
        for x in sorted(ws.keys()):
            cifra=int(x[1])
            bias=float(bs["b"+str(cifra)])
            dotproduct=np.sum(np.multiply(test_set[i],ws[x]))+bias
            raspunsuri.append(dotproduct)
        index_raspuns=raspunsuri.index(max(raspunsuri))
        if index_raspuns==labels_test[i]:
            nr_corecte+=1

    print nr_corecte
    return (nr_corecte*100)/len(test_set)

start=time.time()
antrenament()
end=time.time()
print ("Timp executie antrenament: "+str(end-start))

start=time.time()
print test()
end=time.time()
print ("Timp executie test: "+str(end-start))
