import os
import hashlib
import distance
import numpy as np
import random
from bitstring import BitArray
from random import randint
from Crypto.Hash import MD2


def swap_bit(arr, random_position):
    if arr[random_position-1] == 1:
        arr[random_position-1] = 0
    else:
        arr[random_position-1] = 1
    return arr

# it creates a string that is 16 bytes long
number = os.urandom(16)
bin_rep = bin(int(os.urandom(16).encode('hex'), 16))
#print bin_rep
#print "Length of the binary is: " + str(len(bin_rep))

#print int(bin_rep, 2)
#print "Length of the decimal is: " + str(len(str(int(bin_rep, 2))))

# take a random number between 0 and 128
random_position = randint(0, 128)
print "The random position is: " + str(random_position)

# flip a bit at a specific position

# flipped_number = bin_rep ^ (1 << random_position)
# print flipped_number

#arr = list(map(int, str(bin_rep)))
#print arr

# without 0b
print bin_rep[2:]
bin_rep = bin_rep[2:]
#print len(bin_rep[2:])
arr1 = list(map(int, bin_rep))
#print arr1
arr2 = swap_bit(arr1, random_position)
#print arr2

bin_rep2 = "".join(str(x) for x in arr2)
print bin_rep2

print len(bin_rep)
print len(bin_rep2)

print "The Hamming Distance is: " + str(distance.hamming(bin_rep, bin_rep2))
md2_hash_value_1 = MD2.new(bin_rep).hexdigest()
md2_hash_value_2 = MD2.new(bin_rep2).hexdigest()
print "MD2 hash for value_1: " + str(md2_hash_value_1)
print "MD2 hash for value_2: " + str(md2_hash_value_2)
print "The Hamming Distance between hashes is: " + str(distance.hamming(md2_hash_value_1,md2_hash_value_2))

'''
MD2("The quick brown fox jumps over the lazy dog") = 
 03d85a0d629d2c442e987525319fc471

  MD2("The quick brown fox jumps over the lazy cog") = 
 6b890c9292668cdbbfda00a4ebf31f05
 '''

'''
string1 = "The quick brown fox jumps over the lazy dog"
string2 = "The quick brown fox jumps over the lazy cog"
md2_hash_value_1 = MD2.new(string1).hexdigest()
md2_hash_value_2 = MD2.new(string2).hexdigest()
print md2_hash_value_1
print md2_hash_value_2
print "---------------"
print distance.hamming(md2_hash_value_1, md2_hash_value_2)
print distance.hamming("03d85a0d629d2c442e987525319fc471","6b890c9292668cdbbfda00a4ebf31f05")
print md2_hash_value_1 == "03d85a0d629d2c442e987525319fc471"
print md2_hash_value_2 == "6b890c9292668cdbbfda00a4ebf31f05"
'''

# Se selecciona la posicion de la cadena a cambiar.
pos = random.randint(0,127)
# Se genera la cadena aleatoria de 256 bits de longitud
x1 = random.getrandbits(128)
print x1

# Creamos la mascara apropiada y se la aplicamos a la primera
# cadena para crear la cadena casi identica
mask = 1 << pos
x2 = x1 ^ mask
print x2

# Generamos las cadenas de bits a partir de los enteros generados
m1 = BitArray(uint=x1, length=128)
m2 = BitArray(uint=x2, length=128)



print m1
print m2
print distance.hamming(m1,m2)
md2_hash_value_1 = MD2.new(str(m1)).hexdigest()
md2_hash_value_2 = MD2.new(str(m2)).hexdigest()
print "MD2 hash for value_1: " + str(md2_hash_value_1)
print "MD2 hash for value_2: " + str(md2_hash_value_2)
print distance.hamming(md2_hash_value_1, md2_hash_value_2)

