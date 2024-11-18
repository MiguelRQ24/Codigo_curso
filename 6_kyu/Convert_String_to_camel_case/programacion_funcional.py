def to_camel_case(text):
    lista_palabras = text.replace('-','_').split('_')
    return lista_palabras[0] + ''.join(map((lambda palabra: palabra.capitalize()), lista_palabras[1:]))