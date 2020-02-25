import clean

s = 683324890805829105256759883887052508552354821874
h = 0xe87288d30ba2e4b042c334e54a14620f467d213c
x = 0xc0ffee
r = 968122975261745054561805511895297282641641279955
q = 0xf4f47f05794b256174bba6e9b396a7707e563c5b
print("modular inverse: " + str(clean.modularInverse(s, q)))
print("k = " + str((clean.modularInverse(s, q)*(h+x*r)) % q))
