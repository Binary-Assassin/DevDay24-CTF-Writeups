from Crypto.Util.number import bytes_to_long
import random


with open('flag.txt', 'r') as file:
    flag = file.read()

plaintext = flag
plaintext_bytes = plaintext.encode()

# Convert the bytes to an integer
m = bytes_to_long(plaintext_bytes)

def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)

        # fermat's little theorem for prime test
        if pow(2, p - 1, p) == 1:
            return p

bits = 1024
p = generate_prime(bits)
n = p * p * p
e = 65537
ciphertext = pow(m, e, n)

print("Ct:", ciphertext)
print("n: ",n)

