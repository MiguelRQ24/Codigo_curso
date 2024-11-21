def anagrams(word, words):
    alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
    anagramas = []
    for palabra in words:
        cantidad_letras_word = []
        cantidad_letras = [] 
        for letra in alfabeto:
            cantidad_letras_word.append(word.count(letra))
            cantidad_letras.append(palabra.count(letra))
        if cantidad_letras_word == cantidad_letras:
            anagramas.append(palabra)        
    return anagramas
print(anagrams('alla', ['aall', 'alal', 'llaa', 'alll', 'llll', 'aaal', 'alllaaallla', 'lala', 'assa', 'affa', 'asaa', 'nnww']))

def anagrams_sort(word, words):
    return [palabra for palabra in words if sorted(palabra) == sorted(word) ]
print(anagrams_sort('alla', ['aall', 'alal', 'llaa', 'alll', 'llll', 'aaal', 'alllaaallla', 'lala', 'assa', 'affa', 'asaa', 'nnww']))