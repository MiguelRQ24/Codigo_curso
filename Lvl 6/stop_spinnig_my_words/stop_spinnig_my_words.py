def spin_words(sentence):
    
    MIN_LON_GIRAR = 5
    
    frase = ""
    for palabra in sentence.split(" "):
        if len(palabra) >= MIN_LON_GIRAR:
            frase += " " + palabra[::-1]
        else :
            frase += " " + palabra
            
    return frase.lstrip()