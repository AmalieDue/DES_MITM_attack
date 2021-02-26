#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:41:47 2021

@author: amalieduejensen
"""

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



        
        
        