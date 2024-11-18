def check_sudoku(sudoku):
    numero_vueltas = 0                                              # acumulador del numero de vueltas
    while numero_vueltas < len(sudoku):
        numeros_columna = []
        for linea in sudoku:                                        # lee cada fila del sudoku 
            if len(linea) == len(set(linea)):                       # si hay numeros repetidos devuelve falso sino: 
                numeros_columna.append(linea[numero_vueltas])       # mete un numero de la fila (que este en la posicion = al numero de vueltas) en numeros_columna  
            else :
                return False
            if len(numeros_columna) != len(set(numeros_columna)):   # checkea que no se repita ningun numero en la columna
                return False
            for numero in linea:                                    # checkea las condiciones de las filas
                if type(numero) != int:                             #------> if not instance(numero, int)
                    return False
                elif numero > len(linea) or numero < 0:             # comprueba que el numero no sea mayor el maximo o el minimo permitido
                    return False
                elif len(linea) != len(sudoku):                  # comprueba si hay alguna linea que mida mas o menos que el resto
                    return False
                else:
                    continue
        numero_vueltas += 1                                         
    return True


def check_sudoku(sudoku):                                              
    for linea in sudoku:                                        # lee cada fila del sudoku
        for numero in linea:                                    # checkea las condiciones de las filas
                if type(numero) != int:                             #------> if not instance(numero, int)
                    return False
                elif numero > len(linea) or numero < 0:             # comprueba que el numero no sea mayor el maximo o el minimo permitido
                    return False
                elif len(linea) != len(sudoku):                  # comprueba si hay alguna linea que mida mas o menos que el resto
                    return False
                else:
                    continue
    numero_vueltas = 0                                              # acumulador del numero de vueltas
    while numero_vueltas < len(sudoku):
        numeros_columna = []
        for linea in sudoku:                                        # lee cada fila del sudoku
            if len(linea) == len(set(linea)):                       # si hay numeros repetidos devuelve falso sino: 
                numeros_columna.append(linea[numero_vueltas])       # mete un numero de la fila (que este en la posicion = al numero de vueltas) en numeros_columna  
            else :
                return False
            if len(numeros_columna) != len(set(numeros_columna)):   # checkea que no se repita ningun numero en la columna
                return False
        numero_vueltas += 1                                         
    return True