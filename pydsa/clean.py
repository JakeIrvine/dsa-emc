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

#Function to define P, Q and g
def defineParams():
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
    return P, Q, g

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

# Now for the DSA functions that carry out key generation, signing and verification

# Define a function to generate a DSA private and public key pair.
def keyGen(P, Q, g):
    while True:
        privKey = int(input("Enter Private Key : "), 0)
        if 1<privKey<Q-1:
            break
        else:
            print("Please enter an integer between 1 and " + Q-1+"\n\n")

    pubKey = pow(g,privKey,P) # Compute the public key, pub_key = (g ^ priv_key) mod P
    return privKey,pubKey

# Define a function to sign a message, m, with a private key, priv_key.
def sign(m,priv_key):
    H = hashFunction(m) # Compute the hash of the message
    r = 0
    s = 0
    
    while r == 0 or s == 0:

        k = random.randint(1,Q-1) # Choose a random integer k
            
        k_inv = modularInverse(k,Q) # Compute k^-1 mod Q
            
        # Add code to compute r = (g ^ k mod P) mod Q 
            
        r = pow(g,k,P)%Q 
            
        # Add code to compute s = (k_inv * (H + priv_key*r)) mod Q
            
        s = (k_inv *(H + priv_key*r))%Q

    return r,s

# Define a function to verify a signature, sig, on a message, m, with public key, pub_key.

def verify(sig,m,pubKey):
    r,s = sig

    if 0>r or r >Q or 0>s or s>Q:
        return False	
	
    H = hashFunction(m) # Compute the hash of the message
	
    s_inv = modularInverse(s,Q) # Compute s^-1 mod Q 
	
    # Add code to compute v = (g ^ (H*s_inv mod Q) * y ^ (r*s_inv mod Q)) mod P mod Q
	
    v = (pow(g,H*s_inv%Q)* pow(pubKey, r*s_inv%Q))%P%Q 

    # Add code to check that v == r
	
    if v==r: 
        return True
	
    else:
        return False

# Code testing: generate a key pair
P,Q,g = defineParams()

privKey,pubKey = keyGen(P, Q, g)

print("private key =", privKey)
print("public key =", pubKey)

# Code testing: sign a message with the private key generated

message = "hello"
signature = sign(message,privKey)
print("signature = (r,s) =", signature)


# Code testing: verify the signature with the public key generated

verification = verify(signature,message,pubKey)

print("verification =", verification)
