def duplicate_encode(word): 
    return ''.join([')' if word.upper().count(caracter) > 1 else '(' for caracter in word.upper()])