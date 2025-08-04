from graphviz import Digraph

# Simplificador de operadores
def simplificar_expresion(regex):
    resultado = ""
    i = 0
    while i < len(regex):
        c = regex[i]
        if i + 1 < len(regex):
            siguiente = regex[i + 1]
            if siguiente in ['+', '?'] and c == ')':
                count = 0
                j = i
                while j >= 0:
                    if regex[j] == ')':
                        count += 1
                    elif regex[j] == '(':
                        count -= 1
                    if count == 0:
                        break
                    j -= 1
                grupo = regex[j:i+1]
                if siguiente == '+':
                    resultado = resultado[:-(i - j + 1)]
                    resultado += f"{grupo}{grupo}*"
                else:
                    resultado = resultado[:-(i - j + 1)]
                    resultado += f"({grupo}|ε)"
                i += 2
                continue
            elif siguiente == '+':
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

def agregar_concatenacion(regex):
    resultado = ""
    for i in range(len(regex) - 1):
        c1, c2 = regex[i], regex[i + 1]
        resultado += c1
        if (c1 not in '(|' and c2 not in ')*|'):
            resultado += '.'
    resultado += regex[-1]
    return resultado

def infix_to_postfix(expresion):
    precedencia = {'*': 3, '.': 2, '|': 1}
    salida, pila = [], []
    for c in expresion:
        if c.isalnum() or c == 'ε':
            salida.append(c)
        elif c == '(':
            pila.append(c)
        elif c == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            if not pila:
                raise ValueError("Paréntesis desbalanceados.")
            pila.pop()
        else:
            while pila and pila[-1] != '(' and precedencia.get(pila[-1], 0) >= precedencia.get(c, 0):
                salida.append(pila.pop())
            pila.append(c)
    while pila:
        if pila[-1] == '(':
            raise ValueError("Paréntesis desbalanceados.")
        salida.append(pila.pop())
    return ''.join(salida)

# Nodo para AST
class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho

def construir_ast(postfija):
    pila = []
    for c in postfija:
        if c in '*':
            nodo = Nodo(c, izquierdo=pila.pop())
        elif c in '.|':
            derecho = pila.pop()
            izquierdo = pila.pop()
            nodo = Nodo(c, izquierdo, derecho)
        else:
            nodo = Nodo(c)
        pila.append(nodo)
    return pila[-1]

def dibujar_ast(nodo, grafo=None, contador=[0]):
    if grafo is None:
        grafo = Digraph(format='png')
        grafo.attr('node', shape='circle')
    
    id_nodo = str(contador[0])
    grafo.node(id_nodo, nodo.valor)
    contador[0] += 1

    if nodo.izquierdo:
        id_izq = str(contador[0])
        dibujar_ast(nodo.izquierdo, grafo, contador)
        grafo.edge(id_nodo, id_izq)
    if nodo.derecho:
        id_der = str(contador[0])
        dibujar_ast(nodo.derecho, grafo, contador)
        grafo.edge(id_nodo, id_der)

    return grafo

with open("expresiones.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.read().splitlines()

for i, expresion in enumerate(lineas, start=1):
    print(f"\n➤ Expresión {i}: {expresion}")

    simplificada = simplificar_expresion(expresion)
    print(f"  ➤ Simplificada: {simplificada}")

    con_concatenacion = agregar_concatenacion(simplificada)
    print(f"  ➤ Con concatenación: {con_concatenacion}")

    try:
        postfija = infix_to_postfix(con_concatenacion)
        print(f"  ➤ Postfija: {postfija}")
    except ValueError as e:
        print(f"  ❌ Error: {e}")
        continue

    ast = construir_ast(postfija)
    grafo = dibujar_ast(ast)
    grafo.render(f"AST_expresion_{i}", cleanup=True)
    print(f"  ✅ AST generado: AST_expresion_{i}.png")
