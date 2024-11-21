def decode_morse(morse_code):
    CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
            '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
            '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q',
            '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V',
            '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
            
            '-----': '0', '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6',
            '--...': '7', '---..': '8', '----.': '9',
            ' ': ' ' , '/': ' ', '.-.-.-': '.', '--..--': ',', '---...': ':',
            '..--..': '?', '.----.': "'", '-....-': '-', '-..-.': '/', '.--.-.': '@',
            '-...-': '=', '-.--.': '(', '-.--.-': ')', '.-.-.': '+', '...-..-': '$', '.-...' : '&',
            '...---...' : 'SOS', '-.-.--': '!', '..--.-' : '_',  '.-..-.' :'"', '-.-.-.' : ';'}
    signos_decodificado = ''
    palabras = morse_code.lstrip().rstrip().split("   ")
    for (posicion, palabra) in enumerate(palabras):
        letras = palabra.split(' ')
        for letra in letras:
            signos_decodificado += CODE[letra]   
        if posicion == 0 and len(palabras) == 1 or posicion == len(palabras) - 1:
            continue
        else:
            signos_decodificado += ' '
    return signos_decodificado