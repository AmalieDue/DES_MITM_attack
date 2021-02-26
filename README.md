# DES Meet-in-the-Middle Attack

> This repository contains our implementatino of the meet-in-the-middle attack on DES in the course 02255 Modern Cryptology Spring 2021 at DTU. The group members are [Anders Lammert Hartmann](https://github.com/AndersHartmann) 
(Student ID: s153596) and [Amalie Due Jensen](https://github.com/AmalieDue) (Student ID: s160503).

## Structure

The project has been divided into the following files:

* `DES.py`: Contains all function related to DES and the attack.
* `main.py`: The main program.

## Usage

A simple example of encryption and decryption with 2DES is shown below.

```python

import DES as D
import random

random.seed(1)

# Generate two keys. They contain 20 random bits each, and then padded with 0's
# such that they get the correct size
k1=random.getrandbits(20)
k1=bin(k1)
k1=k1[2:]
k1=D.pad_key(k1)

k2=random.getrandbits(20)
k2=bin(k2)
k2=k2[2:]
k2=D.pad_key(k2)

# The keys are converted to bytes
k1=D.bitstring_to_bytes(k1)
k2=D.bitstring_to_bytes(k2)

print("The first key:", k1)
print("The second key:",k2)

```

```python

Out[]:
        The first key: b'\x89\x96\xc0\x00\x00\x00\x00\x00'
        The second key: b'\x91\xb7P\x00\x00\x00\x00\x00'

```

```python

# We define the text that should be encrypted and pad it with spaces
message = b'Hello123'
plaintext=D.pad_text(message)

# Encrypt message
ciphertext=D.Double_DES_encrypt(k1,k2,plaintext)

print("Ciphertext:", ciphertext)
```

```python

Out[]:
        Ciphertext: b'\x05\xc1\xd1\x8eD\xdeA\x00'

```

```python

plaintext = D.Double_DES_decrypt(k1,k2,ciphertext)
print(plaintext)

```

```python

Out[]:
        Plaintext: b'Hello123'

```

Success! We have encrypted and decrypted.


A simple example of how to do a MITM attack is shown below.

```python

import DES as D
import random

random.seed(1)

# Generate two keys. They contain 20 random bits each, and then padded with 0's
# such that they get the correct size
k1=random.getrandbits(20)
k1=bin(k1)
k1=k1[2:]
k1=D.pad_key(k1)

k2=random.getrandbits(20)
k2=bin(k2)
k2=k2[2:]
k2=D.pad_key(k2)

# The keys are converted to bytes
k1=D.bitstring_to_bytes(k1)
k2=D.bitstring_to_bytes(k2)

print("The first key:", k1)
print("The second key:",k2)

```

```python

Out[]:
        The first key: b'\x89\x96\xc0\x00\x00\x00\x00\x00'
        The second key: b'\x91\xb7P\x00\x00\x00\x00\x00'

```

```python
# We define the text that should be encrypted and pad it with spaces
message = b'Hello123'
plaintext=D.pad_text(message)

# Encrypt message
ciphertext=D.Double_DES_encrypt(k1,k2,plaintext)

# Perform MITM attack. The goal is to derive the key pair
PKP=D.MITM(plaintext,ciphertext)

print("Possible key pairs\n")
print(PKP)

for i in range(len(PKP)): 
    if PKP[i][0]==k1 and PKP[i][1]==k2:
        print("Found the correct key pair\n")
        print("k1\n",PKP[i][0])
        print("k2\n",PKP[i][1])
        break
    
    if i==len(PKP)-1:
        print("Error: Did not find the correct key pair")

```

```python

Out[]:
        Possible key pairs

        [[b'\x88\x96\xc0\x00\x00\x00\x00\x00', b'\x91\xb7P\x00\x00\x00\x00\x00'],
        
        [b'\x88\x97\xc0\x00\x00\x00\x00\x00', b'\x91\xb7P\x00\x00\x00\x00\x00'], 
        
        [b'\x89\x96\xc0\x00\x00\x00\x00\x00', b'\x91\xb7P\x00\x00\x00\x00\x00'], 
        
        [b'\x89\x97\xc0\x00\x00\x00\x00\x00', b'\x91\xb7P\x00\x00\x00\x00\x00']]
        
        Found the correct key pair

        k1
        b'\x89\x96\xc0\x00\x00\x00\x00\x00'
        k2
        b'\x91\xb7P\x00\x00\x00\x00\x00'

```

Success! We found the correct key pair.

## API