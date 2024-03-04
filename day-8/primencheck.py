def primechecker(number):
    isPrime = True
    for i in range(2,number):
        if number % i ==0:
            isPrime = False
    if isPrime:
        print("it is prime number ")
    else:
        print("it is not a prime number") 
                   