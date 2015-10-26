# -*- coding: utf-8 -*-



# # Affiche les tables de multiplication de 1 a N 
# L = range(1, 3 + 1) # L est la liste [1, 2, ..., n]
# for i in L :
# 	for j in L : print i * j,
# 	print


# Multiplie un nombre par le resultat du produit du precedent N fois

# def factoriel(x) :
# 	if x == 0 : return 1
# 	L = range (1, x + 1)
# 	s = 1
# 	for i in L :
# 		s = s * i
# 		# print s
# 	return s

# print (" factoriel de 3 est de : ")
# print factoriel(3)
# print (" factoriel de 5 est de : ")
# print factoriel(5)
# print (" factoriel de 2 est de : ")
# print factoriel(2)
# print

# def binom(n,m) :
# 	return (factoriel(n)/(factoriel(n-m)*factoriel(m)))
# print ("Le coef binomial est de : ")
# print binom(5,3)



# def somme_des_entiers_pairs(n) :
# 	L = range(n+1) # L = [0, 1,..., n]
# 	l = len(L) #la longueur de la liste L
# 	i = s = 0
# 	while (i!= l) :
# 		if i % 2 == 0 : s = s + i
# 		i = i + 1
# 	return s, L

# for i in range(10) : print somme_des_entiers_pairs(10)[1][i],
# print "la somme des elements pair la liste est", somme_des_entiers_pairs(10)[0]

# ---------- PGCD ----------
def euclid(a,b):
	a = abs(a)
	b = abs(b)
	while (b > 0):
		r=a%b
		a = b
		b = r
	return a

print "euclide : ",euclid(15,9)

# print 150/46
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
	return a,u0,v0

print "euclide  extend : " , extended_euclid(15,9)