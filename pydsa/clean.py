import random
import hashlib
import math
from tqdm import tqdm



def checkPrime(num):
    lim = math.ceil(math.sqrt(num))
    for i in range(2, lim):
        if num%i == 0:
            print (i)
            return False
    return True

#Function to define P, Q and g
def defineParams():
    P = int(input("Enter your P : "), 0)
    Q = int(input("Enter your Q : "), 0)
    g = int(input("Enter your g : "), 0)
    privKey = int(input("Enter your private key : "), 0)
    pubKey = int(input("Enter your public key : "), 0)

    P = 0x800000000000000089e1855218a0e7dac38136ffafa72eda7859f2171e25e65eac698c1702578b07dc2a1076da241c76c62d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebeac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc871a584471bb1
    Q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
    g = 0x5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119458fef538b8fa4046c8db53039db620c094c9fa077ef389b5322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a0470f5b64c36b625a097f1651fe775323556fe00b3608c887892878480e99041be601a62166ca6894bdd41a7054ec89f756ba9fc95302291
    privKey = 0xc0ffee
    pubKey = 0x71ce056d249efd15fd1d0aa1db97cc9944b4f8b5d7b5e23a75426629c26d0bbadf70e11fbc79040f57ff44b5aa468bfa8e2e726ba3b7718a89cfc78cd45eda98f8e145d3848855cd925ec13e3d44a88c2492dda293b40239ff6a265a381679a44d2a1393fcaab9d56a541d0db94e67260b40cb01b28fb856b8e18876de470ff4


    print ("\n\n")
    return P, Q, g, privKey, pubKey

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
# Not used for decryption
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
	
    # Add code to compute s v = (g ^ (H*s_inv mod Q) * y ^ (r*s_inv mod Q)) mod P mod Q

    v = (pow(g, H*s_inv % Q, P) * pow(pubKey, r*s_inv % Q, P)) % P % Q



    print(v)

    # Add code to check that v == r
	
    if v==r: 
        return True
	
    else:
        return False

# Code testing: generate a key pair
P,Q,g,privKey,pubKey = defineParams()



# Code testing: sign a message with the private key generated
message = input("Message : ")
signature = sign(message,privKey)
print("signature = (r,s) =", signature)


# Code testing: verify the signature with the public key generated

verification = verify(signature,message,pubKey)

print("verification =", verification)
