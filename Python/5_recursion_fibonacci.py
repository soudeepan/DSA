# recursive function of fibonacci 
def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  

nterms = int(input("Enter number of terms: "))  

# print series

print("Fibonacci sequence:")  
for i in range(nterms):  
    print(recur_fibo(i))  