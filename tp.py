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
	mult = [[0] * n for _ in range(n)]
	tab_inversible = []
	for ligne in range (0,n):
		for col in range(0,n):
			mult[ligne][col] = (ligne * col)%n
			if mult[ligne][col] == 1:
				tab_inversible.append(ligne) 
	return tab_inversible

n=10
print "Les inversibles modulo ",n," sont:", inversibles(n)

def ordre(a,n):
	if euclid(a,n) == 1:
		cpt = 1
		while (a**cpt)%n != 1:
			cpt=cpt+1
	return cpt

n=9
a=2
print "l'ordre de ",a," modulo ",n," est ",ordre(a,n)

def generateur(n):
	phi = naive_euler_function(n)
	tab_invers=inversibles(n)
	i=0
	while ordre(tab_invers[i],n) != phi:
		i+=1
	g = tab_invers[i]
	return g

n=17
print "Un generateur modulo ",n," est ",generateur(n)

def CRT(L1,L2):
	if len(L1) == len(L2):
		produit_mod = 1
		tab_mod_inv = []
		tab_prod_partiel = []
		total = 0
		# Calcul le produit modulaire
		for i in range(0,len(L1)):
			produit_mod = produit_mod * L1[i]
		# Calcul de l'inverse modulaire
		for i in range(0,len(L1)):
			calc = produit_mod/L1[i]
			tab_prod_partiel.append(calc)
			mod = modular_inverse(calc,L1[i])
			tab_mod_inv.append(mod)
		# On fait multiplication du produit_mod, de l'inverse mod et de l'entier
		for i in range(0,len(L1)):
			total += L2[i]*tab_prod_partiel[i]*tab_mod_inv[i]
		r=total%produit_mod
	return r
L1=[2,3,5] #modulo
L2=[1,2,4]
x=CRT(L1,L2)
print "CRT(",L1,",",L2,")=",x
print "Verification:"
k=len(L1)
for i in range(0,k):
	print x," mod ",L1[i],"=",L2[i],"? -->",(x%L1[i])==(L2[i]%L1[i])

def naive_exponentiation(a,k,n):
	if k > 0:
		n = abs(n)
		res = a
		for i in range(1,k):
			res = (res * a) %n
	else:
		res = 1
	return res

a=-2
k=6
n=-10
print a,"^",k," mod ",n," = ", naive_exponentiation(a,k,n)

# Fonctionne
def square_and_multiply(a,k,n):
	n = abs(n)
	h = 1
	bits = '{0:b}'.format(k)
	size = len(bits)
	i=0
	while i < size:
		h = (h*h)%n
		if bits[i] == 1:
			h = (h*a)%n
		i = i + 1
	return h

print a,"^",k," mod ",n," = ", square_and_multiply(a,k,n)
def miller_rabin(n,p):
	assert n >= 2
	if n == 2:
		return True
	if n < 6:  # On optimise pour des petits nombres connus 
		return [False, False, True, True, False, True][n]
	elif n & 1 == 0: 
		return False
	
	s = 0
	d = n - 1
	while d & 1 == 0:
		s = s + 1
		d = d >> 1
	for i in range(0,p) :
		a = random.randint(2,n-2)
		x = square_and_multiply(a, d, n)
		if x != 1 and x + 1 != n:
			for r in xrange(1, s):
				x = square_and_multiply(x, 2, n)
				if x == 1:
					return False 
				elif x == n - 1:
					a = 0  
					break  #On continue les tests malgre que tout semble OK 
			if a:
				return False  
	return True  
 

n=13 # nombre a tester 
p=80 # precision
for i in range(2,30):
	print "miller_rabin(",i,",",p,")=",miller_rabin(i,p)


def generate_prime(k,p):
	N = random.getrandbits(k)
	while miller_rabin(N,p) == False:
		print N, miller_rabin(N,p)		
		N = random.getrandbits(k)
	return N

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





