# recursion function for GCD
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    return int(a*b / gcd(a,b))
    
x = 120
y = 32
print("GCD of",x,y,"is",gcd(x,y))
print("LCM of",x,y,"is",lcm(x,y))