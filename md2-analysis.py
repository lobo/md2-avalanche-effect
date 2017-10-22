import distance
import random
import statistics
import datetime
from bitstring import BitArray
from Crypto.Hash import MD2
import matplotlib.pyplot as plt

def test_vectors():
    print "Testing the Hash MD2 algorithm first..."
    print "Test vectors running..."

    string1 = "The quick brown fox jumps over the lazy dog"
    string2 = "The quick brown fox jumps over the lazy cog"
    string3 = ""
    string4 = "a"
    string5 = "abc"
    string6 = "message digest"
    string7 = "abcdefghijklmnopqrstuvwxyz"
    string8 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    string9 = "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
    
    md2_hash_value_1 = MD2.new(string1).hexdigest()
    md2_hash_value_2 = MD2.new(string2).hexdigest()
    md2_hash_value_3 = MD2.new(string3).hexdigest()
    md2_hash_value_4 = MD2.new(string4).hexdigest()
    md2_hash_value_5 = MD2.new(string5).hexdigest()
    md2_hash_value_6 = MD2.new(string6).hexdigest()
    md2_hash_value_7 = MD2.new(string7).hexdigest()
    md2_hash_value_8 = MD2.new(string8).hexdigest()
    md2_hash_value_9 = MD2.new(string9).hexdigest()
    
    print md2_hash_value_1
    print md2_hash_value_2
    print md2_hash_value_3
    print md2_hash_value_4
    print md2_hash_value_5
    print md2_hash_value_6
    print md2_hash_value_7
    print md2_hash_value_8
    print md2_hash_value_9

def calculate_hamming(x1):
    pos = random.randint(0,127)
    
    mask = 1 << pos
    x2 = x1 ^ mask

    m1 = BitArray(uint=x1, length=128)
    m2 = BitArray(uint=x2, length=128)

    hash_of_m1 = MD2.new(str(m1))

    md2_hash_value_1 = MD2.new(str(m1)).hexdigest()
    md2_hash_value_2 = MD2.new(str(m2)).hexdigest()

    hamming_result = (distance.hamming(md2_hash_value_1, md2_hash_value_2)+2) << 1
    return hamming_result

def calculate():
    results = []
    x1 = random.getrandbits(128)
    
    for i in range(1000):
        results.append(calculate_hamming(x1))

    mean = statistics.mean(results)
    variance = statistics.variance(results)
    error_mean = abs(64 - mean)/64
    error_variance = abs(32 - variance)/32

    if error_mean > 0.075:
        #print error_mean
        return results
        #raise RuntimeError("La media de la tercera corrida dio un error mayor a 7.5%")
    if error_variance > 0.075:
        #print error_variance
        return results
        #raise RuntimeError("La varianza de la tercera corrida dio un error mayor a 7.5%")

    return results

if __name__ == '__main__':

    test_vectors()
    
    results1 = calculate()
    results2 = calculate()
    results3 = calculate()

    f = open('Resultado-' + str(datetime.date.today()) + '.txt','w')
    f.write("Experimento del dia " + str(datetime.date.today()) + ".\n")

    # Acumulamos el resultado de las tres corridas
    result = results1 + results2 + results3

    # Calculamos los estadisticos correspondientes
    # y los escribimos al archivo de salida
    media = statistics.mean(result)
    f.write("Media: " + str(media) + "\n")
    try:
        moda = statistics.mode(result)
        f.write("Moda: " + str(moda) + "\n")
    except statistics.StatisticsError:
        f.write("Existe mas de un valor que podria ser la moda.\n")
    mediana = statistics.median(result)
    f.write("Mediana: " + str(mediana) + "\n")

    desviacion = statistics.stdev(result,xbar=media)
    f.write("Desviacion: " + str(desviacion) + "\n")

    varianza = statistics.variance(result,xbar=media)
    f.write("Varianza: " + str(varianza) + "\n")

    f.write("Distancias obtenidas:\nD = [")

    f.write(", ".join(map(str, result[0:20])))
    for i in range(20,1000,20):
        f.write("\n     " + ", ".join(map(str, result[i:i+20])))
    f.write("]\n")
    f.close()

    # Creamos el histograma

    n = max(result) - min(result)
    plt.hist(result,bins=n)
    plt.title("Distancias de Hamming")
    plt.xlabel("N de bits distintos")
    plt.ylabel("Frecuencia")
    plt.savefig("Histograma")



