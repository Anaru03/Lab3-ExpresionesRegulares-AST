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
            elif siguiente == '?':
                resultado += c + '|ε'
                i += 2
                continue
        resultado += c
        i += 1
    return resultado


def get_precedence(op):
    precedences = {'*': 3, '.': 2, '|': 1}
    return precedences.get(op, 0)

def format_regex(regex):
    formatted = ""
    for i in range(len(regex)):
        c1 = regex[i]
        formatted += c1
        if i + 1 < len(regex):
            c2 = regex[i + 1]
            if (c1 not in '(|' and c2 not in '|)*'):
                formatted += '.'
    return formatted

def infix_to_postfix(regex):
    stack = []
    output = ""
    for c in regex:
        if c.isalnum() or c == 'ε':
            output += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()  # Quita el '('
        else:
            while stack and get_precedence(c) <= get_precedence(stack[-1]):
                output += stack.pop()
            stack.append(c)
    while stack:
        output += stack.pop()
    return output

if __name__ == "__main__":
    expresion = "a+b?(c|d)*"
    print("Expresión original:        ", expresion)

    simplificada = simplificador_expresiones(expresion)
    print("Tras simplificar operadores:", simplificada)

    formateada = format_regex(simplificada)
    print("Tras formatear con '.':     ", formateada)

    postfija = infix_to_postfix(formateada)
    print("Expresión postfija:         ", postfija)
