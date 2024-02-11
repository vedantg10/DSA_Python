def SumNumbers(n):
    if n==1:
        return n
    else:
        return n + SumNumbers(n-1)
    

print(SumNumbers(5))    



def sumOfDigits(n):
    if n <=0:
        return 0
    else:
        return n%10 + sumOfDigits(n//10)
    
print(sumOfDigits(448))