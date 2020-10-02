def HCF(a,b):
    if(b==0):
        return a
    else:
        return HCF(b, b%a)

def LCM(a,b):
    return a*b/HCF(a,b)

def isPrime(n):
    if(n==1):
        return False
    elif(n==2 or n==3):
        return True
    
    if(n%2==0 or n%3==0):
        return False

    i=5
    while(i*i<=n):
        if(n%i==0 or n%(i+2)==0):
            return False
        else:
            i+=6
    return True