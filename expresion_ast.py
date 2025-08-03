def simplificador_expresiones(regex):
    resultado = ""
    i = 0
    while i < len(regex):
        c = regex[i]
        if i + 1 < len(regex):
            siguiente = regex[i + 1]
            if siguiente == '+':
                resultado += c + c + '*'
                i += 2
                continue
        resultado += c
        i += 1
    return resultado
