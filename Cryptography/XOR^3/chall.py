from pwn import xor
import random

x1_bytes = bytes([random.randint(0, 255) for _ in range(32)])
x2_bytes = bytes([random.randint(0, 255) for _ in range(32)])
x3_bytes = bytes([random.randint(0, 255) for _ in range(32)])

x1_hex = x1_bytes.hex()
x2_hex = x2_bytes.hex()
x3_hex = x3_bytes.hex()

flag = b'DD24{TrY_H4rd3r_N3v3r_G1v3_Up}'

print("key1:",x1_hex)
print("key2:",xor(bytes.fromhex(x1_hex),bytes.fromhex(x2_hex)).hex())
print("key3:",xor(bytes.fromhex(x2_hex),bytes.fromhex(x3_hex)).hex())
print("ciphertext:",xor(flag,bytes.fromhex(x1_hex),bytes.fromhex(x2_hex),bytes.fromhex(x3_hex)).hex())
