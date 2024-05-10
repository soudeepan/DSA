# recursive function of factorial 
def factiorial(n):
    if n == 1:
        return 1
    else:
        return n*factiorial(n-1)
    
num = int(input("Enter a number: "))
print("Factorial of",num,"is",factiorial(num))
