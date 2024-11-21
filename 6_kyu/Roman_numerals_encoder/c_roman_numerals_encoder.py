def solution(numero_decimal):
    numero_romano = ""
    exponente_base_diez = len(str(numero_decimal)) - 1
    valores_romanos = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}
    for digito in str(numero_decimal):
        base_diez = int(digito) * 10 ** (exponente_base_diez)
        if base_diez in valores_romanos:
            numero_romano += valores_romanos[base_diez]
        elif int(digito) <= 3:
            numero_romano += valores_romanos[1 * 10 ** exponente_base_diez] * int(digito)
        elif int(digito) == 4:
            numero_romano += valores_romanos[1 * 10 ** (exponente_base_diez)] + valores_romanos[5 * 10 ** (exponente_base_diez)]         
        elif 9 > int(digito) > 5:
            numero_romano += valores_romanos[5 * 10 ** exponente_base_diez] + valores_romanos[1 * 10 ** exponente_base_diez] * (int(digito) - 5)
        else :
            numero_romano += valores_romanos[1 * 10 ** (exponente_base_diez)] + valores_romanos[10 * 10 ** (exponente_base_diez)]    
        exponente_base_diez -= 1
    return numero_romano

if __name__ == "__main__":
    assert solution(1) == 'I', "solution(1),'I'"
    assert solution(4) == 'IV', "solution(4),'IV'"
    assert solution(6) == 'VI', "solution(6),'VI'"
    assert solution(14) == 'XIV', "solution(14),'XIV"
    assert solution(21) == 'XXI', "solution(21),'XXI'"
    assert solution(89) == 'LXXXIX', "solution(89),'LXXXIX'"
    assert solution(91) == 'XCI', "solution(91),'XCI'"
    assert solution(984) == 'CMLXXXIV', "solution(984),'CMLXXXIV'"
    assert solution(1000) == 'M', 'solution(1000), M'
    assert solution(1889) == 'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'"
    assert solution(1989) == 'MCMLXXXIX', "solution(1989),'MCMLXXXIX'"
    assert solution(3999) == 'MMMCMXCIX'
