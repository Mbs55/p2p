import random as r
import math
import datetime as dt
import base64
from sympy import isprime
def PrimeNum():
    while(True):
        num=r.getrandbits(512)
        if(isprime(num)):
            return num


def pq():
    p=PrimeNum()
    q=PrimeNum()
    while(p==q):
        q=PrimeNum()
    return p,q    
def exponent(p,q):
    n=p*q
    phi=(p-1)*(q-1)
    for i in range(2,n):
        if(math.gcd(i,n)==1 and math.gcd(i,phi)==1):
            return i
def decrypt(e,phi):
        return pow(e,-1,phi)
def public_key(n,e):
    pk=f"n={n},e={e},creation_date:{dt.datetime.now()}"
    bytes_str=pk.encode("utf-8")
    bs64=base64.b64encode(bytes_str)
    with open("./KeyPair/public_key.txt","w") as f:
        f.write("-------------------------------------My Public Key-------------------------------------\n")
        f.write(str(bs64)) 
        f.write("\n-------------------------------------End Of My Public Key-------------------------------------\n")

def private_key(phi,d):
    pk=f"phi={phi},d={d},creation_date:{dt.datetime.now()}"
    bytes_str=pk.encode("utf-8")
    bs64=base64.b64encode(bytes_str)
    with open("./KeyPair/private_key.txt","w") as f:
        f.write("-------------------------------------My Private Key-------------------------------------\n")
        f.write(str(bs64)) 
        f.write("\n-------------------------------------End Of My Private Key-------------------------------------\n")
def keyPair():
    p,q=pq()
    n=p*q
    phi=(p-1)*(q-1)
    e=exponent(p,q)
    d=decrypt(e,phi)
    public_key(n,e)
    private_key(phi,d)

if __name__=="__main__":
    print("Generating the keys...")
    keyPair()

        








