from Crypto.Hash import MD2
import random, struct, math

# ------------------------ Useful functions ----------------------- 
def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def decimal_to_binary(num):
    if num == 0:
        return "" 
    return decimal_to_binary(num//2) + str(num % 2) 

# ------------------------ Main Program -----------------------
def main_program():
    iterations = 10000          
    minimum_num = 64 # FIPS 180-4 SHS 08/2015
    beginning = 2**5          
    end = beginning + iterations 
    output = ""
    for i in range(beginning,end):
        print 50*'-'
        data_1 = decimal_to_binary(i-1)
        data_2 = decimal_to_binary(i)
        print "data_1: " + str(data_1)
        print "data_2: " + str(data_2)
        value_1 = str((minimum_num-len(data_1))*"0" + data_1)
        value_2 = str((minimum_num-len(data_2))*"0" + data_2)
        print "value_1: " + str(value_1)
        print "value_2: " + str(value_2) 

        md2_hash_value_1 = MD2.new(value_1).hexdigest()
        md2_hash_value_2 = MD2.new(value_2).hexdigest()
        print "MD2 hash for value_1: " + str(md2_hash_value_1)
        print "MD2 hash for value_2: " + str(md2_hash_value_2)
        print "Hamming Distance is: " + str(hamming_distance(md2_hash_value_1,md2_hash_value_2))
        output += str(hamming_distance(md2_hash_value_1,md2_hash_value_2))+";"
        iterations -= 1

    hamilton_num = map(int, output.split(';')[:-1])
    print 50*"-"


    # ------------------------ Stats -----------------------
    
    # Promedio
    media = sum(hamilton_num)/float(len(hamilton_num))
    print "Media: " + str(media)

    # Moda                                                                                   
    iterations = 0                                                                         
    for i in hamilton_num:                                                                              
       appearances = hamilton_num.count(i)                                                             
       if appearances > iterations:                                                       
           iterations = appearances                                                       
                                                                                         
    modas = []                                                                               
    for i in hamilton_num:                                                                              
        appearances = hamilton_num.count(i)                                                             
        if appearances == iterations and i not in modas:                                   
            modas.append(i)                                                                  
                                                                                         
    print "Moda: ", modas                                                                     
                                                                                         
    # Mediana                                                                                
    hamilton_num.sort()                                                                                                                                                                 
                                                                                         
    if len(hamilton_num) % 2 == 0:                                                                      
        n = len(hamilton_num)                                                                           
        mediana = (hamilton_num[n/2-1]+ hamilton_num[n/2] )/2                                                      
    else:                                                                                    
        mediana =hamilton_num[len(hamilton_num)/2]                                                                 
                                                                                         
    print 'Mediana: ',mediana 

    # Varianza
    suma = 0
    for i in hamilton_num:
        suma += (media - float(i))**2
    varianza = float(suma)/len(hamilton_num) 
    print 'Varianza: ',varianza

    # Desviacion estandar
    desviacion_estandar = math.sqrt(varianza)
    print 'Desviacion estandar: ',desviacion_estandar


main_program()