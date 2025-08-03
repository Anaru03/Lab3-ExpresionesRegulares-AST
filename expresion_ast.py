def simplificador_expresiones(regex):
    resultado = ""
    i = 0
    while i < len(regex):
        c = regex[i]
        resultado += c
        i += 1
    return resultado
