def move_zeros(lista):
    ceros =  []
    sin_ceros = list(lista)
    for numero in lista:
        if numero == 0:
            ceros.append(sin_ceros.pop(sin_ceros.index(0)))
    return sin_ceros + ceros