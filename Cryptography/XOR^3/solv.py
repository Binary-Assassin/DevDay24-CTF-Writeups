from pwn import xor

key1= 'c45d6f5563562e4d9106e1ef3b0e56fbe39bff2b8250a79c26bb116da1ad239f'
key2= 'f52021aff2dea228befbafa69dfb33b8101f8c57a915223c537378f16f8fd326'
key3= '97fd10243ff73274321beea943d8766a5455b382fa8ff430ee76ffd66202f83f'
ciphertext= '17e44d4527f5740afc4c7a771bbd7fd3c5fe3bc7278763fe97879bd6b39a849025c50d2e08e97966ef7c553f27b210d6ca'

# Convert hexadecimal strings to bytes
x1 = bytes.fromhex(key1)
x2 = xor(bytes.fromhex(key2), x1)
x3 = xor(bytes.fromhex(key3), x2)

# Decrypt the ciphertext
flag = xor(bytes.fromhex(ciphertext), x1, x3, x2)

print(flag.decode())
