# inverse of a under modulo m
 
# A naive method to find modulor
# multiplicative inverse of 'a'
# under modulo 'm'

def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1
a = int(input("Enter a : "))
m = int(input("Enter m : "))
print(modInverse(a, m))
# This code is contributed by Nikita Tiwari.