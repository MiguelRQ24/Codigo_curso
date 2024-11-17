def encoder(secuencia_letras):
    letras_repetidas = ""
    posicion_letras = { 0 : ''}
    secuencia_codificada = ""
    for letra in secuencia_letras:
            if letras_repetidas :
                letras_repetidas += letra
                if letras_repetidas in posicion_letras.values():
                    continue
                else:
                    posicion_letras[len(posicion_letras)] = letras_repetidas
                    for (lugar, letras) in posicion_letras.items():
                        if letras == letras_repetidas[:-1]: # busca el resto de letras, sin contar la actual, en el diccionario para ponerlo en la secuencia codificada como numero
                            secuencia_codificada += f'{lugar}' + letras_repetidas[-1]
                        else:
                           continue
                    letras_repetidas = ""
            else :
                if letra in posicion_letras.values():
                    letras_repetidas += letra
                else:
                    posicion_letras[len(posicion_letras)] = letra
                    secuencia_codificada += '0' + letra
    if letras_repetidas:
        for (lugar, letras) in posicion_letras.items():
            if letras == letras_repetidas:
                secuencia_codificada += f'{lugar}'
    return secuencia_codificada  

def decoder(secuencia_codificada):
    numero = ''
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numero_letra = [(0, '')]
    for (posicion, caracter) in enumerate(secuencia_codificada):
            if caracter in numeros:

                numero += caracter
                if posicion == len(secuencia_codificada) - 1:
                    numero_letra.append((int(numero), ''))
            else:
                numero_letra.append((int(numero), caracter))
                numero = ''

    secuencia_descodificada = ''
    for posicion, pareja in enumerate(numero_letra):
        if pareja[0] == 0:
            secuencia_descodificada += pareja[1]
        else: 
            letras = ''
            numero_letra_siguiente =  numero_letra[posicion][0]
            letras += pareja[1]
            while numero_letra_siguiente != 0:
                    letras += numero_letra[numero_letra_siguiente][1]
                    numero_letra_siguiente = numero_letra[numero_letra_siguiente][0]
            letras += numero_letra[numero_letra_siguiente][1]
            secuencia_descodificada += letras[::-1]
            letras = ''
    return secuencia_descodificada

if __name__ == "__main__":
        assert encoder('ABAABABAABAB') == '0A0B1A2A4A4B' , 'ABAABABAABAB'
        assert encoder('ABAABABAABABAA')== '0A0B1A2A4A4B3', 'ABAABABAABABAA'
        assert encoder('ABBCBCABABCAABCAABBCAA')== '0A0B2C3A2A4A6B6', 'ABBCBCABABCAABCAABBCAA'
        assert encoder('AAAAAAAAAAAAAAA')== '0A1A2A3A4A', 'AAAAAAAAAAAAAAA'
        assert encoder('ABCABCABCABCABCABC')== '0A0B0C1B3A2C4C7A6', 'ABCABCABCABCABCABC'
        assert encoder('ABCDDEFGABCDEDBBDEAAEDAEDCDABC')== '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C', 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC'

        assert decoder('0A0B1A2A4A4B')== 'ABAABABAABAB', '0A0B1A2A4A4B'
        assert decoder('0A0B1A2A4A4B3')== 'ABAABABAABABAA', '0A0B1A2A4A4B3'
        assert decoder('0A0B2C3A2A4A6B6')== 'ABBCBCABABCAABCAABBCAA', '0A0B2C3A2A4A6B6'
        assert decoder('0A1A2A3A4A')== 'AAAAAAAAAAAAAAA', '0A1A2A3A4A'
        assert decoder('0A0B0C1B3A2C4C7A6')== 'ABCABCABCABCABCABC', '0A0B0C1B3A2C4C7A6'
        assert decoder('0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C')== 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC', '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C'