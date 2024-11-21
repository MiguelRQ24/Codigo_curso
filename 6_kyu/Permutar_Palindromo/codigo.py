def permute_a_palindrome(input):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    cantidad_letras = []
    num_letras_impares = 0
    for letra in alfabeto:
        cantidad_letras.append(input.count(letra))  
    for cantidad in cantidad_letras :
            if cantidad / 2 != int(cantidad / 2) :
                num_letras_impares = num_letras_impares + 1
    if num_letras_impares > 1 :
        return False
    else :
        return True
