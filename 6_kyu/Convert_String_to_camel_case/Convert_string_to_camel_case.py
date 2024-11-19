def to_camel_case(text):
    texto_en_lista = list(text)
    for caracter in texto_en_lista :
        if caracter == '-' :
            texto_en_lista[texto_en_lista.index(caracter)] = '_'
    lista_palabras = ''.join(texto_en_lista).split(' ')
    for palabra in lista_palabras :
        if lista_palabras.index(palabra) > 0 :
            lista_palabras[lista_palabras.index(palabra)] = palabra.capitalize()
    return ''.join(lista_palabras)

def to_camel_case(text):
    lista_palabras = text.replace('-','_').split('_')
    for posicion, palabra in enumerate(lista_palabras):
        if lista_palabras.index(palabra) > 0 :
            lista_palabras[posicion] = palabra.capitalize()
    return ''.join(lista_palabras)