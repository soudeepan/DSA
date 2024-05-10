# recursive function for power
def power(a,b):
    if b == 1:
        return a
    else:
        return a*power(a,b-1)
    
a = 4
b = 2

print(a,"to the power",b,"is",power(a,b))
