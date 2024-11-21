def repeats(arr):
    suma_numeros_unicos = 0
    for numero in arr :
        if arr.count(numero) == 1 :
            suma_numeros_unicos += numero
    return suma_numeros_unicos


def repeats_comprimida(arr):
    # sum([numero for numero in arr if arr.count(numero) == 1]) 
    return sum([numero if arr.count(numero) == 1 else 0 for numero in arr]) 


print(repeats_comprimida([3,3,4,4,5,5,7,8,10,1000000]))
