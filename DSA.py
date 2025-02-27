#1. Fibonacci Series

def fibo(n):

    a =0
    b =1
    temp =0

    if n > 0 and n < 2 :
        print(a)
        return

    if n > 1 and n < 3:
        print(a,b)
        return
        
    for i in range(1,n):
        
        print(a)
        temp = a
        a = b
        b = temp+b

#fibo(6)

#2. Factorial Number

def factorial(n):

    fact =1 

    for i in range(1,n+1):
        fact = fact * i
        print(i)


    print(fact)

factorial(4)


#3. IsPrimeNo

def isPrimeNo(num):


    no = int(num/2 +1)
    for i in range(2,int(num/2 +1)):

        if (num % i ==0):
            print(num," is not a prime number")
            return
    
    print(num," is prime number")

isPrimeNo(15)

#4. 