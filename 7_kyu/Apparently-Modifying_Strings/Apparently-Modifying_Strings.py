def apparently(st):
    palabras = st.split()
    frase = ''
    for posicion, palabra in enumerate(palabras):
        if palabra == "and" or palabra == "but":
            if posicion == len(palabras) - 1:
                frase += palabra + ' apparently '
            elif palabras[posicion + 1] == 'apparently':
                frase += palabra + ' '
            else:
                frase += palabra + ' apparently '
        else:
            frase += palabra + ' '
    return frase.rstrip()