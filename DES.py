#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 09:16:26 2021

@author: andershartmann
"""

from Crypto.Cipher import DES

#We define a function that pad's the text to match the correct block size. 
def pad_text(text):
    n = len(text) % 8
    return text + (b' ' * n)

#We define a function that pads the 2 bit keys with zeros. 
def pad_key(key):
    return key + '0' * (64 - len(key))

#We define a function that makes a bitstring into bytes
def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')


###########################################################################################################

#We define a function that perfors double DES encryption
def Double_DES_encrypt(k1,k2,plaintext):
    des1 = DES.new(k1, DES.MODE_ECB)
    des2 = DES.new(k2, DES.MODE_ECB)
    
    E1=des1.encrypt(plaintext)
    E2=des2.encrypt(E1)
    
    return E2

#We define a function that perfors double DES decryption
def Double_DES_decrypt(k1,k2,ciphertext): 
    des1 = DES.new(k1, DES.MODE_ECB)
    des2 = DES.new(k2, DES.MODE_ECB)
    
    D1=des2.decrypt(ciphertext)
    D2=des1.decrypt(D1)
    
    return D2

###########################################################################################################

#First we define a function adding two binary strings together
def add_binary_nums(x, y): 
        max_len = max(len(x), len(y)) 
  
        x = x.zfill(max_len) 
        y = y.zfill(max_len) 
          
        # initialize the result 
        result = '' 
          
        # initialize the carry 
        carry = 0
  
        # Traverse the string 
        for i in range(max_len - 1, -1, -1): 
            r = carry 
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result 
            carry = 0 if r < 2 else 1     # Compute the carry. 
          
        if carry !=0 : result = '1' + result 
  
        return result.zfill(max_len) 

##########################################################################################################
        
#We define a function that generates a set of all possible DES keys. 
def Key_generator(): 
    Keys=[]
    b='1'
    init='00000000000000000000'
    Keys.append(bitstring_to_bytes(pad_key(init)))
    
    for i in range(1,2**20):
        init=add_binary_nums(init,b)
        Keys.append(bitstring_to_bytes(pad_key(init)))
    
    return Keys


######################################################################################################################################################################################################################

#We define a function that can perform a binary search. 
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high+low) //2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

###########################################################################################################
        
#We define a function that performs a meet in the middle attack on double DES. 
def MITM(plaintext,ciphertext): 
    
    keys=Key_generator()
    
    Encrypted_values=[]
    Decrypted_values_with_keys=[]
    Possible_key_pairs=[]
    
    for i in range(2**20): 
        k1=keys[i]
        
        des = DES.new(k1, DES.MODE_ECB)
        Encrypted_values.append(des.encrypt(plaintext))
        Decrypted_values_with_keys.append([des.decrypt(ciphertext),k1])
        
    Decrypted_values_with_keys.sort()

    test_arr=[Decrypted_values_with_keys[i][0] for i in range(len(Decrypted_values_with_keys))]
    
    for i in range(2**20): 
        
        check=Encrypted_values[i]
        
        index=binary_search(test_arr, 0, len(Decrypted_values_with_keys)-1, check)
        
        if index!=-1: 
            Possible_key_pairs.append([keys[i],Decrypted_values_with_keys[index][1]])
           
    return Possible_key_pairs
     

#######################################################################################################################################################
