# -*- coding: utf-8 -*-

import random
from math import *


#********************
#
# fonctions arithmétiques
#
#********************

def euclid(a,b):
	a = abs(a)
	b = abs(b)
	while (b > 0):
		r=a%b
		a = b
		b = r
	return a

print "euclid(4321554,315432512)=",euclid(4321554,315432512)
print "euclid(1234,0)=",euclid(1234,0)
print "euclid(1234,1)=",euclid(1234,1)
print "euclid(-4321554,315432512)=",euclid(-4321554,315432512)
print "euclid(4321554,-315432512)=",euclid(4321554,-315432512)
print "euclid(-4321554,-315432512)=",euclid(-4321554,-315432512)

# Retourne le PGCD et 2 coef de Bezout
def extended_euclid(a,b):
	d = euclid(a,b)
	u0 ,u1 = 1,0
	v0,v1 = 0,1
	while (b != 0):
		r=a%b
		q = a//b
		a,b = b,r
		u0,u1 = u1,u0 - q * u1
		v0,v1 = v1, v0 - q * v1

	if (a < 0) : return -a,-u0,-v0
	else : return a,u0,v0
	

# print "euclide  extend : " , extended_euclid(15,9)

a=4321554
b=315432512
r=extended_euclid(a,b)
print "extended_euclid(",a,",",b,")=",r
print "verification:",  r[0]==r[1]*a+r[2]*b 

a=-4321554
b=-315432512
r=extended_euclid(a,b)
print "extended_euclid(",a,",",b,")=",r
print "verification:",  r[0]==r[1]*a+r[2]*b 

a=-4321554
b=315432512
r=extended_euclid(a,b)
print "extended_euclid(",a,",",b,")=",r
print "verification:",  r[0]==r[1]*a+r[2]*b 

a=4321554
b=-315432512
r=extended_euclid(a,b)
print "extended_euclid(",a,",",b,")=",r
print "verification:",  r[0]==r[1]*a+r[2]*b 

# N ==> modulo
def modular_inverse(a,n):
	if euclid(a,n) != 1 : return 0
	else :
		r = extended_euclid(a,n)
		bezout = r[1]
		if bezout < 0 : bezout = bezout+ abs(n)
		return bezout
			
a=53
n=101
r=modular_inverse(a,n)
print "modular_inverse(",a,",",n,")=",r
print "verification positif :",  r>=0
print "verification 1:", r*a % abs(n)==1 

a=-53
n=-101
r=modular_inverse(a,n)
print "modular_inverse(",a,",",n,")=",r
print "verification positif :",  r>=0
print "verification 1:", r*a % abs(n)==1 

def euler_function(L1,L2):
	phi=1
	for i in range(0,len(L1)) :
		# n = n + L1[i]**L2[i]
		if L2[i] != 0 :
			phi = phi * (L1[i] - 1)*L1[i]**(L2[i]-1)
	return phi
	

L1=[2,3,5]
L2=[2,0,2]
print "euler_function(",L1,",",L2,")=",euler_function(L1,L2)

def naive_euler_function(n):
	count = 0
	for i in range(1,n):
		phi = euclid(i,n)
		if phi == 1:
			count = count+1

	return count

n=100
print "naive_euler_function(",n,")=",naive_euler_function(n)

def tables(n):
	maxi = n-1
	# Ligne - Colonne
	tab = [[0] * n for _ in range(n)]
	mult = [[0] * n for _ in range(n)]
	for ligne in range (0,n):
		for col in range(0,n):
			tab[ligne][col] = (ligne + col)%n
			mult[ligne][col] = (ligne * col)%n
	print "TAB ADDITION"
	print tab

	print "TAB multiplication"
	print mult

tables(5)

def inversibles(n):
	return []

n=10
print "Les inversibles modulo ",n," sont:", inversibles(10)

def ordre(a,n):
	return 0

n=9
a=2
print "l'ordre de ",a," modulo ",n," est ",ordre(a,n)

def generateur(n):
	return 0

n=17
print "Un generateur modulo ",n," est ",generateur(n)

def CRT(L1,L2):
	return 0

L1=[2,3,5]
L2=[1,2,4]
x=CRT(L1,L2)
print "CRT(",L1,",",L2,")=",x
print "Verification:"
k=len(L1)
for i in range(0,k):
	print x," mod ",L1[i],"=",L2[i],"? -->",(x%L1[i])==(L2[i]%L1[i])

def naive_exponentiation(a,k,n):
	return 0

a=2
k=8
n=10
print a,"^",k," mod ",n," = ", naive_exponentiation(a,k,n)

def square_and_multiply(a,k,n):
	return 0

print a,"^",k," mod ",n," = ", square_and_multiply(a,k,n)

def miller_rabin(n,p):
	return False

n=13
p=80
print "miller_rabin(",n,",",p,")=",miller_rabin(n,p)

def generate_prime(k,p):
	return 2

k=100
p=80
prime=generate_prime(k,p)
print "generate_prime(",k,",",p,")=",prime
print "nombre de bits:", floor(log(prime,2))+1


#********************
#
# fonctions RSA
#
#********************

def generate_key(k):
	p,q,n,phi,d,e = 0,0,0,0,0,0
	return p,q,n,phi,d,e

def encipher(m,n,e):
	return 0


def decipher(c,d,n):
	return 0

def generate_key_CRT(k):
	return  #à préciser

def decipher_CRT(): #paramètres à préciser
	return 0 


#********************
#
# fonctions de factorisation
#
#********************

def trial_division(n):
	p,q=0,0
	return p,q

def fermat(n):
	p,q=0,0
	return p,q

def pollard(n):
	p,q=0,0
	return p,q

def rsa_factoring(n,e):
	return 0



#********************
#
# petit exposant secret
#
#********************

#voici un exemple non trivial qui fonctionne

n=20340839661827
d=5
e=20340839661827

# dans cette partie, vous devrez développer 
# d'autres fonctions

def small_exponent(n,e):
	return d





