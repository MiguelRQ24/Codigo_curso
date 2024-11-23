def merge(*dicts):
    diccionario_conjunto = {}
    for diccionario in dicts:
        for clave in diccionario:
            if clave not in diccionario_conjunto:
                diccionario_conjunto[clave] = [diccionario[clave]]
            else :
                diccionario_conjunto[clave] += [diccionario[clave]]
    return diccionario_conjunto