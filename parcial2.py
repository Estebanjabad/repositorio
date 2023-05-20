import math
import numpy
import random

def ejercicio1():
    U=random.random()
    vals=[0.24,0.33,0.64,1]
    for i in range(4):
        if (U<vals[i]):
            return i

def ejercicio2(sims):
    generated_vals=[]
    count=0
    for x in range(sims):
        U=random.random()
        if (U<0.5):
            generated_vals.append(U*4)
        else:
            generated_vals.append(1/(1-U))
    for i in generated_vals:
        if (i <= 3):
            count+=1
    print(count/sims)


def geometrica(p):
    U = random.random()
    return int(math.log(1-U)/math.log(1-p))+1

def geopdf(n):
    p=0.6
    return p*((1-p)**(n-1))


def ejercicio3(sims):
    c=1.0000001
    for x in range(sims):
        U=random.random()
        Y=geometrica(0.6)
        while (True):
            pX=geopdf(Y)/0.999999989004884     #P(X=y)  =  P(Y=y|Y<=20)
            if (U<(geopdf(Y)/(pX*c))):
                print (Y)
                break
            else:
                continue



def ejercicio4(sims):
    count=0
    for x in range(sims):
        total=0
        for _ in range(1000):
            U0=random.random()
            if (U0<0.05):
                U = 1-random.random()
                val= -math.log(U)*800
                total+=val
        if (total>50000):
            count+=1
    print(count/sims)
print("Ej1")
print(ejercicio1())
print("Ej2")
ejercicio2(10000)
print("Ej3")
ejercicio3(10)
print("Ej4")
ejercicio4(10000) 
