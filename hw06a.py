def findMaxPrime(x):
    f = 2
    maxprime = 2
    while f <= x:
        if (x%f==0):
            maxprime = f
            x = x/f
        else:
            f = f+1
    print maxprime

findMaxPrime(600851475143)
