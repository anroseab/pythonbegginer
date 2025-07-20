def fact(n):
    result =1
    for i in range(n,0,-1):
        result=result*i
    return result
#print(fact(5))

def FACT(n):
    if n==0:
        return 0
    else:
        return n* FACT(n-1)
print(FACT(5))