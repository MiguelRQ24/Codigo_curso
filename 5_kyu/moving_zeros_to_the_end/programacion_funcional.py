def move_zeros(lista):
    sin_ceros = list(lista)
    return sin_ceros + [sin_ceros.pop(sin_ceros.index(0)) for numero in lista if numero == 0]
