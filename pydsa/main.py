import random # We need to import the random module to generate random numbers during key and signature generation. We'll use the randint function from the random module to do this.
import hashlib # We'll use hash functions from the hashlib module to hash our messages.


# Define the parameters 

P = 283
Q = 47
g = 60


# Define a function to hash our messages
# This hash function is "sha1"
# To change the hash function swap "sha1" on line two, for "md5", "sha224", "sha256", "sha384" or "sha512"
# The first three lines hash the message m
# In the fourth line, we convert the hash output to an integer

def hash_function(m):
    m = m.encode()
    h = hashlib.sha1()
    h.update(m)
    hashed_message = int(h.hexdigest(),16)
    return hashed_message


# Define a modular inverse function 
# This function finds the modular inverse of a mod N, denoted a^-1 mod N
# We use "Fermat's Little Theorem" to make this computation simple and so this function only works when N is prime
# (In general, throughout this code, calculate a^b mod N with the "pow" function: a^b mod N = pow(a,b,N))

def modular_inverse(a,N):
    a_inv = pow(a,N-2,N)
    return a_inv


# Now for the DSA functions that carry out key generation, signing and verification

# Define a function to generate a DSA private and public key pair.

def key_generation():
    priv_key = random.randint(1,Q-1) # Compute the private key
	
    pub_key = pow(g,priv_key,P) # Compute the public key, pub_key = (g ^ priv_key) mod P

    return priv_key,pub_key

# Define a function to sign a message, m, with a private key, priv_key.

def sign(m,priv_key):
    H = hash_function(m) # Compute the hash of the message
    r = 0
    s = 0
    
    while r == 0 or s == 0:

        k = random.randint(1,Q-1) # Choose a random integer k
            
        k_inv = modular_inverse(k,Q) # Compute k^-1 mod Q
            
        # Add code to compute r = (g ^ k mod P) mod Q 
            
        r = pow(g,k,P)%Q 
            
        # Add code to compute s = (k_inv * (H + priv_key*r)) mod Q
            
        s = (k_inv*(H+priv_key*r))%Q

    return r,s

# Define a function to verify a signature, sig, on a message, m, with public key, pub_key.

def verify(sig,m,pub_key):
    r,s = sig

    # Add code to check whether 0<r<Q and 0<s<Q, otherwise the signature is rejected.
	
    if 0<r<Q and 0<s<Q:
        return False	
	
    H = hash_function(m) # Compute the hash of the message
	
    s_inv = modular_inverse(s,Q) # Compute s^-1 mod Q 
	
    # Add code to compute v = (g ^ (H*s_inv mod Q) * y ^ (r*s_inv mod Q)) mod P mod Q
	
    v = (pow(g,H*s_inv%Q)%P)%Q 

    # Add code to check that v == r
	
    if v==r: 
        return True
	
    else:
        return False
		
		
# Code testing: generate a key pair

private_key,public_key = key_generation()

print("private key =", private_key)
print("public key =", public_key)


# Code testing: sign a message with the private key generated

message = "hello"

signature = sign(message,private_key)

print("signature = (r,s) =", signature)


# Code testing: verify the signature with the public key generated

verification = verify(signature,message,public_key)

print("verification =", verification)

