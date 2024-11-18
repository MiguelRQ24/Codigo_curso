def duplicate_encode(word): 
    parentesis = ''
    for caracter in word.upper() :
        if word.upper().count(caracter) > 1 :
            parentesis = parentesis + ')'
        else : 
            parentesis = parentesis + '('
    return parentesis