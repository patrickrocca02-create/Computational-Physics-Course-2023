import numpy as np


def main():

    n=input("Numero di intervalli:\n")
    n=int(n)

    h=2*np.pi/n
    
    f = open("derivata_seno.tsv",mode='w')
    fe = open("errore_derivata_seno.tsv",mode='w')

    f.write("x\tder_exact\tder_oh2\tder_0h4\n")
    
    for i in range(n):
        x=i*h
        
        fxp=np.sin(x+h)
        fxm=np.sin(x-h)

        derx_exact=np.cos(x)
        derx_oh2=(fxp-fxm)/(2*h)
        
        fxpp = np.sin(x+2*h)
        fxmm = np.sin(x-2*h)
        derx_oh4=(-fxpp+8*fxp-8*fxm+fxmm)/(12*h)

    
        f.write(str(x)+"\t"+str(derx_exact)+"\t"+ str(derx_oh2)+ "\t" + str(derx_oh4) + "\n")
        fe.write(str(x)+" "+str(derx_oh2-derx_exact)+" "+str(derx_oh4-derx_exact)+"\n")

    f.close()
    fe.close()

if __name__ == "__main__":
    main()

