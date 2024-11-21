def stock_list(list_of_art, list_of_cat):
    if list_of_art == []:
        return ''
    conteo_tipos = dict.fromkeys(list_of_cat, 0)
    for libro in list_of_art:
        if libro[0] in conteo_tipos:
            conteo_tipos[libro[0]] += int(libro.split(' ')[1])
    return ' - '.join(str(tipo).replace("'", "") for tipo in conteo_tipos.items()).replace(',', ' :')

if __name__ == "__main__":

    b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = ["A", "B"]
    assert stock_list(b, c) == "(A : 200) - (B : 1140)"
    
    b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
    c = []
    assert stock_list(b, c) == ""