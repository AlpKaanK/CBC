import datetime
import socket
import math
import time
import random

def BinModPow(a,n,m):
    b = 1
    apow = a
    while n > 0:
        if n % 2 == 1:
            b = (b * apow) % m
        n = n // 2
        apow = (apow*apow) % m
    return b

def FermatTest(m,n):
    prime = True
    for i in range(0,n):
        a = random.randrange(0,m)
        am = BinModPow(a,m,m)
        if not (am == a % m):
            prime = False
            break
    return prime

def NextPrime(m):
    if m%2 == 0:
        m = m-1
    else:
        m = m-2
    prime = False
    while not prime:
        m = m+2
        prime = FermatTest(m,100)
    return m
def Enc(m,p):
   t = m%2**32
   answer = 0
   cc = iv
   while m>0:
       t = m%2**32
       m = m//2**32
       c = ((g ^ m)^cc % p * q) + ((g ^ m) ^cc % q)
       cc = c
       answer  = 2**64 * answer + c
       print(answer)
   return t
"""
def Enc(K,m):
    c = ((g ^ m) % p * q) + ((g ^ m) % q)
    answer = c ^ iv
    print(answer)
"""
p = NextPrime(random.randrange(2**31,2**32))    #step3
q = NextPrime(random.randrange(2**31,2**32))    #step3
g = random.randrange(2,p)                       #step3
r = random.randrange(2**31,2**32)               #step3
K = (p,q,g,r)
iv = random.randrange(2**63,2**64) #as initial vector , last step

p = NextPrime(p)
q = NextPrime(q)
m = 12345678901234567890123456789012345678901234567890 #step1
Enc(m,p)
print("Message: ",m)

