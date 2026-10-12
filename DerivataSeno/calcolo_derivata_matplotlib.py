'''Programma per calcolare la derivata di sin(x) tra 0 e 2Pi 
tramite differenziazione numerica e grafica con matplotlib'''


import numpy as np
import matplotlib.pyplot as plt


def main():

    n=input("Numero di intervalli:\n")
    n=int(n)

    h=2*np.pi/n #larghezza intervalli

    x=np.zeros((n),dtype=np.float64)
    f=np.zeros((n),dtype=np.float64)
    
    fp=np.zeros((n),dtype=np.float64)
    fm=np.zeros((n),dtype=np.float64)
    fpp = np.zeros((n),dtype=np.float64)
    fmm = np.zeros((n),dtype=np.float64)
    
    der_exact=np.zeros((n),dtype=np.float64)
    der_oh=np.zeros((n),dtype=np.float64)


    for i in range(n):
        x[i]=i*h
        f[i]=np.sin(i*h)
        fp[i]=np.sin(i*h+h)
        fm[i]=np.sin(i*h-h)
        fpp[i]=np.sin(i*h+2*h)
        fmm[i]=np.sin(i*h-2*h)
        der_exact[i]=np.cos(i*h)

    der_oh=(fp-f)/h  #qui sottraggo due vettori elemento per elemento
    der_oh2=(fp-fm)/(2*h) 
    der_oh4=(-fpp+8*fp-8*fm+fmm)/(12*h)


    plt.plot(x,der_exact)
    plt.plot(x,der_oh)
    plt.plot(x,der_oh2)
    plt.plot(x,der_oh4)
    
    plt.show(block=True)
    

if __name__ == "__main__":
    main()