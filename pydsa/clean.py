import random
import hashlib
import math

def menu():
    print ("[1] Enter all Values :")
#Function to check if input num is prime
def checkPrime(num):
    lim = math.ceil(math.sqrt(num))
    for i in range(2, lim):
        if num%i == 0:
            print (i)
            return False
    return True


P = Q = g = True 
while not P and not Q: 
    P = int(input("Enter your P : "), 0)
    if not checkPrime(P):
        P = False

    Q = int(input("Enter your Q : "), 0)
    if not checkPrime(Q):
        Q = False

    elif (P-1)%Q != 0:
        print ("p-1 must be a multiple of Q!")
        P = Q = False

    if not g:
        g = int(input("Enter your g : "), 0)
        g = True
    print ("\n\n")

#Function to hash messages
#options for hashFunc are : sha1, md5, sha224, sha256, sha384, sha512
def hashFunction(text, hashFunc = "sha1"):
    text = text.encode()
    func = getattr(hashlib, hashFunc)    
    h = func()
    h.update(text)
    hashed_message = int(h.hexdigest(), 16)
    return hashed_message


def modularInverse(num, mod):
    return pow(num, mod-2, mod)



