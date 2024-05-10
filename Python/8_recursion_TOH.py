# recursive function for Tower of Hanoi Problem

def toh(a,b,c,n):
    if n == 1:
        print("Move disk from",a,"to",c)
        return
    else:
        toh(a,c,b,n-1)
        toh(a,b,c,1)
        toh(b,a,c,n-1)

ndisk = int(input("Eneter no. of disk: "))
toh("A","B","C",ndisk)