def mix_strings(texto_uno, texto_dos):
    
    letras = []
    for letra in set(texto_uno + texto_dos):
        if letra.isalpha() and letra.islower():
            letras.append(letra)
    
    repeticiones_txt_uno = []
    repeticiones_txt_dos = []
    for letra in letras[::]:
        repeticiones_letra_uno = texto_uno.count(letra)
        repeticiones_letra_dos = texto_dos.count(letra)
        if repeticiones_letra_uno > 1 or repeticiones_letra_dos > 1:
            repeticiones_txt_uno.append(repeticiones_letra_uno)
            repeticiones_txt_dos.append(repeticiones_letra_dos)
        else:
            letras.remove(letra)
    
    repetidas_diferentes_veces = {}
    repetidas_igual_veces = {}
    for posicion, valor in enumerate(repeticiones_txt_uno):
        if valor > repeticiones_txt_dos[posicion]:
            if valor in repetidas_diferentes_veces.keys():
                repetidas_diferentes_veces[valor].append(f'1:{letras[posicion] * valor}')
            else:
                repetidas_diferentes_veces[valor] = list([f'1:{letras[posicion] * valor}'])
        elif valor < repeticiones_txt_dos[posicion]:
            if repeticiones_txt_dos[posicion] in repetidas_diferentes_veces:
                repetidas_diferentes_veces[repeticiones_txt_dos[posicion]].append(f'2:{letras[posicion] * repeticiones_txt_dos[posicion]}') 
            else:
                repetidas_diferentes_veces[repeticiones_txt_dos[posicion]] = list([f'2:{letras[posicion] * repeticiones_txt_dos[posicion]}'])
        else:
            if valor in repetidas_igual_veces:
                repetidas_igual_veces[valor].append(f'=:{letras[posicion] * valor}')
            else:
                repetidas_igual_veces[valor] = list([f'=:{letras[posicion] * valor}'])
    
    repetidas_todas = {}
    repetidas_todas.update(repetidas_diferentes_veces)
    for clave in repetidas_igual_veces:
        if clave in repetidas_todas:
            repetidas_todas[clave].extend(repetidas_igual_veces[clave])
        else:
            repetidas_todas[clave] = repetidas_igual_veces[clave]
    
    texto_codificado = []
    for codigo in sorted(repetidas_todas.keys())[::-1]:
        if isinstance(repetidas_todas[codigo], list):
            texto_codificado.append('/'.join(sorted(repetidas_todas[codigo])))
        else:
            if codigo == max(repetidas_todas):
                texto_codificado.append(repetidas_todas[codigo])
            else:
                texto_codificado.append(('/' + repetidas_todas[codigo]))
    
    return '/'.join(texto_codificado)

if __name__ == "__main__":
    assert mix_strings("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr"
    assert mix_strings("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp") ==  '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'
    assert mix_strings("looping is fun but dangerous", "less dangerous than coding") ==  "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"

    assert mix_strings(" In many languages", " there's a pair of functions") ==  "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
    assert mix_strings("Lords of the Fallen", "gamekult") ==  "1:ee/1:ll/1:oo"
    assert mix_strings("codewars", "codewars") ==  ""
    assert mix_strings("A generation must confront the looming ", "codewarrs") ==  "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"
