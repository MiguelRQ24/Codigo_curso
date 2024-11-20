def first_n_smallest(arr, n):
    a = arr[::-1]
    return [[] if n == 0 else [[min(a)] if n == 1 else [a.pop(a.index(max(a))) if indice < (len(arr) - n) else a for indice in range(len(a)-n+1)][len(arr)-n]][0]][0][::-1]