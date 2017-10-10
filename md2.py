from Crypto.Hash import MD2
import itertools, random, struct, math

# Generate 1000 elements
# Convert them to their binary equivalent

'''
sample_vector_1000_elems = []
charset = "abcdefghijklmnopqrstuvwxyz0123456789"
for i in itertools.product(charset, repeat=6): 
    strMD2 = MD2.new("".join(i)).hexdigest()
    strMD2_to_binary = ''.join(format(x, 'b') for x in bytearray(strMD2))
    print strMD2
    print strMD2_to_binary
    sample_vector_1000_elems.append(strMD2_to_binary)
    if len(sample_vector_1000_elems) == 1000:
        break
'''

def hamdist(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def decimal_a_binario(num):
    ''' Funcion que convierte un decimal en su valor binario '''
    if num == 0:
        return ""
    else:
        return decimal_a_binario(num//2) + str(num % 2) 

def binario_a_decimal(binary):
    ''' funcion que convierte un binario en su valor decimal '''
    decimal = 0
    cont = 0
    print "binary: "+(binary)
    return 0
    binario = str(binary)[::-1];
    print binario
    for digit in binario:
        decimal += (2**int(cont))*int(digit)
        cont +=1
    return decimal

def test():
    '''
    a_str = "just a test string"
    
    assert 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' == sha256().hexdigest()
    assert 'd7b553c6f09ac85d142415f857c5310f3bbbe7cdd787cce4b985acedd585266f' == sha256(a_str).hexdigest()
    assert '8113ebf33c97daa9998762aacafe750c7cefc2b2f173c90c59663a57fe626f21' == sha256(a_str*7).hexdigest()
    
    s = sha256(a_str)
    s.update(a_str)
    assert '03d9963e05a094593190b6fc794cb1a3e1ac7d7883f0b5855268afeccc70d461' == s.hexdigest()
    '''

    SalHam = 0
    SalData = 1
    SalValores = 0
    cant    = 10000          # cantidad a estudiar
    lenc    = 64            # mimimo de seguridad segun FIPS 180-4 SHS 08/2015
    inicio  = 2**5          # inicio indifente mientras cumpla longitud
    fin     = inicio + cant     # fin de la muestra segun la cantidad a estudiar y su inicio
    sal     = ""
    for i in range(inicio,fin):
        if SalData == 1 : print 50*'-'
        dato0   = decimal_a_binario(i-1)
        dato1   = decimal_a_binario(i)
        if SalData == 1 : print "dato0: "+str(dato0)
        if SalData == 1 : print "dato1: "+str(dato1)
        valor0  = str((lenc-len(dato0))*"0"+dato0)
        valor1  = str((lenc-len(dato1))*"0"+dato1)
        if SalData == 1 : print "valor0: "+str(valor0)
        if SalData == 1 : print "valor1: "+str(valor1) 

        str0 = MD2.new(valor0).hexdigest()
        str1 = MD2.new(valor1).hexdigest()
        if SalData == 1 : print "str0: "+str(str0)
        if SalData == 1 : print "str1: "+str(str1)
        if SalData == 1 : print "Distancia de Hamming: "+str(hamdist(str0,str1))
        sal  +=str(hamdist(str0,str1))+";"
        cant -= 1
    if SalHam == 1 : print sal

    SalHamNum = map(int, sal.split(';')[:-1])
    if SalValores == 1 : print 50*"-"
    
    #promedio
    media = sum(SalHamNum)/float(len(SalHamNum))
    if SalValores == 1 : print "media= "+ str(media)

    # moda                                                                                   
    repeticiones = 0                                                                         
    for i in SalHamNum:                                                                              
       apariciones = SalHamNum.count(i)                                                             
       if apariciones > repeticiones:                                                       
           repeticiones = apariciones                                                       
                                                                                         
    modas = []                                                                               
    for i in SalHamNum:                                                                              
        apariciones = SalHamNum.count(i)                                                             
        if apariciones == repeticiones and i not in modas:                                   
            modas.append(i)                                                                  
                                                                                         
    if SalValores == 1 : print "moda:", modas                                                                     
                                                                                         
    # mediana                                                                                
    SalHamNum.sort()                                                                                                                                                                 
                                                                                         
    if len(SalHamNum) % 2 == 0:                                                                      
        n = len(SalHamNum)                                                                           
        mediana = (SalHamNum[n/2-1]+ SalHamNum[n/2] )/2                                                      
    else:                                                                                    
        mediana =SalHamNum[len(SalHamNum)/2]                                                                 
                                                                                         
    if SalValores == 1 : print 'mediana:',mediana 

    #varianza
    suma = 0
    for i in SalHamNum:
        suma += (media - float(i))**2
    varianza = float(suma)/len(SalHamNum) 
    if SalValores == 1 : print 'varianza:',varianza

    # desviacion estandar
    desEstand = math.sqrt(varianza)
    if SalValores == 1 : print 'Desviacion estandar:',desEstand


test()









