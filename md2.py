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

def binary_to_decimal(binary):
    decimal = 0
    cont = 0
    print "binary: " + (binary)
    return 0
    binary_number = str(binary)[::-1];
    print binary_number
    for digit in binary_number:
        decimal += (2**int(cont))*int(digit)
        cont +=1
    return decimal

# ------------------------ Main Program -----------------------
def main_program():
    '''
    a_str = "just a test string"
    
    assert 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' == sha256().hexdigest()
    assert 'd7b553c6f09ac85d142415f857c5310f3bbbe7cdd787cce4b985acedd585266f' == sha256(a_str).hexdigest()
    assert '8113ebf33c97daa9998762aacafe750c7cefc2b2f173c90c59663a57fe626f21' == sha256(a_str*7).hexdigest()
    
    s = sha256(a_str)
    s.update(a_str)
    assert '03d9963e05a094593190b6fc794cb1a3e1ac7d7883f0b5855268afeccc70d461' == s.hexdigest()
    '''

    TRUE = 1
    FALSE = 0
    SalHam = 0
    data_output_enabled = TRUE
    stats_output_enabled = TRUE
    iterations = 10000          
    minimum_num = 64 # FIPS 180-4 SHS 08/2015
    beginning = 2**5          
    end = beginning + iterations 
    output = ""
    for i in range(beginning,end):
        if data_output_enabled == 1 : print 50*'-'
        data_1 = decimal_to_binary(i-1)
        data_2 = decimal_to_binary(i)
        if data_output_enabled == 1 : print "data_1: " + str(data_1)
        if data_output_enabled == 1 : print "data_2: " + str(data_2)
        value_1 = str((minimum_num-len(data_1))*"0" + data_1)
        value_2 = str((minimum_num-len(data_2))*"0" + data_2)
        if data_output_enabled == 1 : print "value_1: " + str(value_1)
        if data_output_enabled == 1 : print "value_2: " + str(value_2) 

        md2_hash_value_1 = MD2.new(value_1).hexdigest()
        md2_hash_value_2 = MD2.new(value_2).hexdigest()
        if data_output_enabled == 1 : print "MD2 hash for value_1: " + str(md2_hash_value_1)
        if data_output_enabled == 1 : print "MD2 hash for value_2: " + str(md2_hash_value_2)
        if data_output_enabled == 1 : print "Hamming Distance is: " + str(hamming_distance(md2_hash_value_1,md2_hash_value_2))
        output += str(hamming_distance(md2_hash_value_1,md2_hash_value_2))+";"
        iterations -= 1
    if SalHam == 1 : print output

    SalHamNum = map(int, output.split(';')[:-1])
    if stats_output_enabled == 1 : print 50*"-"


    # ------------------------ Stats -----------------------
    
    # Promedio
    media = sum(SalHamNum)/float(len(SalHamNum))
    if stats_output_enabled == 1 : print "Media: " + str(media)

    # Moda                                                                                   
    iterations = 0                                                                         
    for i in SalHamNum:                                                                              
       appearances = SalHamNum.count(i)                                                             
       if appearances > iterations:                                                       
           iterations = appearances                                                       
                                                                                         
    modas = []                                                                               
    for i in SalHamNum:                                                                              
        appearances = SalHamNum.count(i)                                                             
        if appearances == iterations and i not in modas:                                   
            modas.append(i)                                                                  
                                                                                         
    if stats_output_enabled == 1 : print "Moda: ", modas                                                                     
                                                                                         
    # Mediana                                                                                
    SalHamNum.sort()                                                                                                                                                                 
                                                                                         
    if len(SalHamNum) % 2 == 0:                                                                      
        n = len(SalHamNum)                                                                           
        mediana = (SalHamNum[n/2-1]+ SalHamNum[n/2] )/2                                                      
    else:                                                                                    
        mediana =SalHamNum[len(SalHamNum)/2]                                                                 
                                                                                         
    if stats_output_enabled == 1 : print 'Mediana: ',mediana 

    # Varianza
    suma = 0
    for i in SalHamNum:
        suma += (media - float(i))**2
    varianza = float(suma)/len(SalHamNum) 
    if stats_output_enabled == 1 : print 'Varianza: ',varianza

    # Desviacion estandar
    desviacion_estandar = math.sqrt(varianza)
    if stats_output_enabled == 1 : print 'Desviacion estandar: ',desviacion_estandar


main_program()









