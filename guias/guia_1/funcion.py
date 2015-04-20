def contar_letra(cadena, letra):
    cnt = 0
    for char in cadena:
        if char==letra: cnt+=1
    return cnt