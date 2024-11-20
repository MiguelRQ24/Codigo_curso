def first_n_smallest(arr, n):
    numeros_pequeños = []
    vueltas = 0
    lista_numeros = list(arr)
    while vueltas < n:
        numeros_pequeños.append(min(lista_numeros))
        lista_numeros.pop(lista_numeros.index(min(lista_numeros)))
        vueltas += 1
    num_peq_ordenados = []
    for numero in arr:
        if numero in numeros_pequeños:
            num_peq_ordenados.append(numero)
            numeros_pequeños.pop(numeros_pequeños.index(numero))
        else:
            continue
    return num_peq_ordenados

    

def first_n_smallest(arr, n):
    numeros = arr[::-1]

    return [numero for numero in [numeros.pop(numeros.index(min(numeros))) for _ in list(numeros) if len(numeros) > (len(numeros) - n) ]]

    return []