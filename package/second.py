def factors(n):
    for num in range(1,n+1):
        if n%num==0:
            print(num,end=" ")

#factors(int(input("Enter the number:")))
def is_perfect(n):
    s=0
    for num in range(1,n+1):
        if n%num==0:
            s+=num
    if s==n:
        return True
    else:return False

    
def factorial(n):
    fact=1
    for num in range(1,n+1):
        fact*=num
    return fact

def is_prime(n):
    count=0
    for num in range(1,n+1):
        if n%num==0:
            count+=1
    if count==2:
        return True
    else:return False
    
    