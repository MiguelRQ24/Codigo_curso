def spin_words(sentence):
    
    MIN_LON_GIRAR = 5
            
    return ' '.join([palabra if len(palabra) >= MIN_LON_GIRAR else palabra[::-1] for palabra in sentence.split(" ")])